"""
Containt all the fonction of the 'IA'
"""
from moves.move_factory import MoveFactory
from moves.enum_moves import Moves
from utils.logger import log

def waifu_player_dangerous(waifu_ia, waifu_player, npc):
    """
    Check if the waifu of the player is dangerous
    :param waifu_ia: Waifu of the IA
    :param waifu_player: Waifu of the player
    :return: True if the waifu of the player is dangerous else False

    dangerous = waifu_player that have moves that are super effective against waifu_ia
    """
    for move in waifu_player.list_of_moves:
        if move.power == 0: continue
        multiplier = get_multiplier(waifu_player, move, waifu_ia)
        if multiplier >= 2:
            return True
    return False

    
def attack_or_switch(waifu_ia, waifu_player, npc, have_to_switch=False):
    """
    Choice the best move for the IA
    """
    if have_to_switch:
        return choice_waifu(waifu_ia, waifu_player, npc), True

    dangerous = waifu_player_dangerous(waifu_ia, waifu_player, npc)

    if dangerous:
        waifu_chosen = choice_waifu(waifu_ia, waifu_player, npc)
        if waifu_chosen == waifu_ia:
            return choice_move(waifu_ia, waifu_player), False
        else :
            return waifu_chosen, True
    else:
        return choice_move(waifu_ia, waifu_player), False



def choice_waifu(waifu_ia, waifu_player, npc):
    """
    Choice the best waifu to send

    Find the waifu that have the best against the waifu of the player
    type on moves advantage
    speed advantage 
    """
    best_waifu = {}

    for waifu in npc.get_alive_waifu():
        if waifu.speed > waifu_player.speed:
            best_waifu[waifu] = 1
        else:
            best_waifu[waifu] = 0
            
        for move in waifu.list_of_moves:
            if move is None: continue
            if move.power == 0: continue
            multiplier = calculate_damage(waifu, move, waifu_player)
            best_waifu[waifu] += multiplier

        for move in waifu_player.list_of_moves:
            if move is None: continue
            if move.power == 0: continue
            multiplier = calculate_damage(waifu_player, move, waifu)
            best_waifu[waifu] -= multiplier

    best_waifu = sorted(best_waifu.items(), key=lambda x: x[1], reverse=True)[0][0]
    
    if best_waifu != waifu_ia:
        waifu_ia.in_fight = False
        best_waifu.in_fight = True

    return best_waifu


def choice_move(waifu_ia, waifu_player):
    """
    Choice if the IA attack or switch
    """
    from random import choice

    if all(move.pp == 0 for move in waifu_ia.list_of_moves):
        waifu_ia.move_to_use = MoveFactory.create_move(Moves.STRUGGLE)
        waifu_ia.move_to_use = best_move
        return waifu_ia


    best_move = None
    highest_damage = float('-inf')

    # Parcourir les attaques de la waifu de l'IA pour trouver celle qui inflige le plus de dégâts
    for move in waifu_ia.list_of_moves:
        if move is None: continue
        if move.pp == 0: continue
        damage = calculate_damage(waifu_ia, move, waifu_player)
        if damage > highest_damage:
            best_move = move
            highest_damage = damage

    if best_move is None:
        best_move = choice(waifu_ia.list_of_moves, lambda move: move.pp > 0)
    
    waifu_ia.move_to_use = best_move
    waifu_ia.move_to_use.pp -= 1

    return waifu_ia


def get_multiplier(attacker, move_used, opponent):

    if any(move_used.type.type_name == type.type_name for type in attacker.types):
        multiplier = 1.5
    else:
        multiplier = 1

    for type_ in opponent.types:
        if move_used.type.type_name in type_.immunities:
            return 0
        
    for op_type in opponent.types:
        if move_used.type.type_name in op_type.weaknesses:
            multiplier *= 2

    for op_type in opponent.types:
        if move_used.type.type_name in op_type.resistances:
            multiplier /= 2

    return multiplier

def calculate_damage(attacker, move_used, opponent):
    
    multiplier = get_multiplier(attacker, move_used, opponent)
    damage = (
        ((2 * attacker.level + 10) / 250)
        * (attacker.attack / opponent.defense)
        * move_used.power
        + 2
    ) * multiplier

    return damage