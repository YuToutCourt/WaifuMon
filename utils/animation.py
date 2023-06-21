from time import sleep

def animation_damage(waifu, damage:int):
    for _ in range(0, round(damage)):
        waifu.hp -= 1
        if waifu.hp <= -1:return
        sleep(0.1)

def animation_heal(waifu, heal:int):
    for _ in range(0, round(heal)):
        waifu.hp += 1
        if waifu.hp >= waifu.hp_max:return
        sleep(0.1)
