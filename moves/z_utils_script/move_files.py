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

for tr in tqdm(trs_list[1:]):
    name = tr.find("a", class_="ent-name").text
    type = tr.find("a", class_="type-icon").text.upper()
    effect = tr.find("td", class_="cell-long-text").text

    if "lowers" in effect.lower() or "raises" in effect.lower():
        current_dir = f"C:/Users/33766/Desktop/Programmation/Python/WaifuMon/moves/stat_modifier_moves/{name.lower().replace(' ', '_')}.py"

        if not os.path.exists(current_dir):
            continue

        destination_dir = f"C:/Users/33766/Desktop/Programmation/Python/WaifuMon/moves/stat_modifier_moves/{type.lower()}_moves"

        if not os.path.exists(destination_dir):
            os.mkdir(destination_dir)

        os.rename(
            current_dir,
            os.path.join(destination_dir, f"{name.lower().replace(' ', '_')}.py"),
        )
