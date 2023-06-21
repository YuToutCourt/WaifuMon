from waifu.waifu import Waifu

def animation_damage(waifu:Waifu, damage:int):
    from time import sleep
    for _ in range(0, round(damage)):
        waifu.hp -= 1
        if waifu.hp == -1:return
        sleep(0.1)