import requests
from bs4 import BeautifulSoup
import os
from tqdm import tqdm

URL = "https://pokemondb.net/move/all"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

tbody = soup.find("tbody")
trs = tbody.find_all("tr")
trs_list = list(trs)

for tr in tqdm(trs_list[2:]):
    # find the a ent-name
    name = tr.find("a", class_="ent-name").text

    # find the a type-icon
    type = tr.find("a", class_="type-icon").text.upper()

    # find all the td cell-num
    tds = tr.find_all("td", class_="cell-num")
    # extract the power, accuracy, pp, proba_effect
    power = tds[0].text
    accuracy = tds[1].text
    pp = tds[2].text
    proba_effect = tds[4].text
    
    if power == "—": power = 0
    if accuracy == "—" or accuracy == "∞": accuracy = 100
    if proba_effect == "—": proba_effect = 100

    effect = tr.find("td", class_="cell-long-text").text
    priority = 0
    if "User attacks first." in effect:
        priority = 1
    # create the file
    with open(os.path.join(f"./{type.lower()}_moves/{name.lower().replace(' ', '_')}.py"), "w") as f:
        f.write(f"from ..move import Move\nfrom waifu_types.type import Type\n\nclass {name.replace(' ', '')}(Move):\n    def __init__(self):\n        super().__init__(\"{name}\", type=Type.{type}, power={power}, accuracy={accuracy}, pp={pp}, priority={priority}, proba_effect={proba_effect})\n\n    def effect(self):\n        \"\"\"\n        {effect}\n        \"\"\"\n        pass\n")