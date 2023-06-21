from character.npc import NPC
from character.player import Player
from waifu.waifu import Waifu
from moves.move import Move
from random import uniform, randint
from utils.logger import log
from typing import Union, List
from utils.handle_input import input_int    
from moves.move_factory import MoveFactory
from moves.enum_moves import Moves
from utils.animation import animation_damage


class Fight:
    def __init__(self, player: Player, npc: NPC):
        self.player = player
        self.npc = npc
        self.tour = 0
        self.finished = False

    def start(self):
        waifu_player = self.player.team[0]
        waifu_enemy = self.npc.team[0]

        waifu_player.in_fight = True
        waifu_enemy.in_fight = True

        self.play_round(waifu_player, waifu_enemy)

    def __check_team_waifu(self, waifu) -> Union[Player, NPC]:
        """
        Check in which team the waifu is
        :param waifu: Waifu to check
        :return: Player or NPC
        """
        for waifu_player in self.player.team:
            if waifu_player == waifu:
                return self.player
        
        for waifu_npc in self.npc.team:
            if waifu_npc == waifu:
                return self.npc
            
        raise Exception("Waifu not found in team")
        
    def __apply_status_before_attack(self, waifu:Waifu):
        if waifu.status is not None and waifu.status.after_attack == False:
            return waifu.status.apply_status()
        return True

    def __apply_status_after_attack(self, waifus:List[Waifu]):
        for waifu in waifus:
            if waifu.status is not None and waifu.status.after_attack:
                waifu.status.apply_status()

    def  __user_choice(self, waifu1, waifu2):
        """
        User choice
        The user can either attack or change waifu
        :param waifu1: Waifu of the player (always)
        :param waifu2: Waifu of the NPC (always)
        """
        choice = input_int("Que voulez-vous faire ?\n1. Attaquer\n2. Changer de waifu\n", 1, 2)
        if choice == 1:
            return waifu1, False
        else:
            return self.player.choice_next_waifu(waifu1), True


    def play_round(self, waifu1: Waifu, waifu2: Waifu):
        if self.finished: return
        log("Tour", self.tour)
        log("Current battle", f"{waifu1.name} vs {waifu2.name}")
        self.tour += 1

        obj = self.__check_team_waifu(waifu1)

        if isinstance(obj, Player):
            waifu1.display_hp()
            waifu1.display_stats()
            waifu2.display_hp()
            waifu2.display_stats()
            waifu1, as_switch  = self.__user_choice(waifu1, waifu2)
            if not as_switch:
                waifu1.choice_move()
            else:
                waifu1.move_to_use = MoveFactory.create_move(Moves.NOTHING)

            waifu2, as_switch = self.npc.handle_choice_during_fight(waifu1, waifu2)
            if as_switch:
                waifu2.move_to_use = MoveFactory.create_move(Moves.NOTHING)

            
        else:
            waifu2.display_hp()
            waifu2.display_stats()
            waifu1.display_hp()
            waifu1.display_stats()
            waifu2, as_switch = self.__user_choice(waifu2, waifu1)
            if not as_switch:
                waifu2.choice_move()
            else:
                waifu2.move_to_use = MoveFactory.create_move(Moves.NOTHING)

            waifu1, as_switch = self.npc.handle_choice_during_fight(waifu2, waifu1)
            if as_switch:
                waifu1.move_to_use = MoveFactory.create_move(Moves.NOTHING)

        attacking_waifu, defending_waifu = self.determine_attack_order(waifu1, waifu2)

        self.attack(attacking_waifu, defending_waifu)

        if defending_waifu.hp <= 0:
            self.handle_knockout(defending_waifu)
            self.__apply_status_after_attack([waifu1, waifu2])
            if attacking_waifu.hp <= 0:
                self.handle_knockout(attacking_waifu)
            return
        
        self.__apply_status_after_attack([waifu1, waifu2])
        if attacking_waifu.hp <= 0:
            self.handle_knockout(attacking_waifu)
            return

        self.play_round(attacking_waifu, defending_waifu)

    def determine_attack_order(self, waifu1: Waifu, waifu2: Waifu):
        if waifu1.move_to_use.priority == waifu2.move_to_use.priority:
            return sorted([waifu1, waifu2], key=lambda waifu: waifu.speed, reverse=True)

        return sorted(
            [waifu1, waifu2], key=lambda waifu: waifu.move_to_use.priority, reverse=True
        )

    def move_effect(self, attacker, defender, move_used):
        # The try/except is here to handle moves that don't have an effect 
        # (because I don't wont to modify all the moves)
        if randint(0, 100) <= move_used.proba_effect:
            try:
                attacker.move_to_use.effect(attacker, defender)
                if defender.hp <= 0:
                    defender.display_hp()
                    return self.handle_knockout(defender)
                if attacker.hp <= 0:
                    attacker.display_hp()
                    return self.handle_knockout(attacker)
            except Exception as e:
                log("Effect Error ", e)

    def attack(self, attacker: Waifu, defender: Waifu, stop=False):
        move_used = attacker.move_to_use

        if not self.__apply_status_before_attack(attacker):
            if attacker.hp <= 0:
              self.move_effect(attacker, defender, move_used)
              return self.handle_knockout(attacker)
            return self.attack(defender, attacker, stop=True)

        log("Attack", f"{attacker.name} use {move_used.name}")
        if randint(0, 100) <= move_used.accuracy:
            damage = self.calculate_damage(attacker, defender)
            # defender.hp -= damage
            animation_damage(defender, damage)
            log(move_used.name, f"{defender.name} a perdu {damage} PV")
            if defender.hp <= 0:
                self.move_effect(attacker, defender, move_used)
                defender.display_hp()
                return self.handle_knockout(defender)
            
            self.move_effect(attacker, defender, move_used)
            if attacker.hp <= 0:
                attacker.display_hp()
                return self.handle_knockout(attacker)
            
            if defender.hp <= 0:
                defender.display_hp()
                return self.handle_knockout(defender)
            
        else:
            print("Le coup n'a pas touché")


        if stop:
            self.__apply_status_after_attack([attacker, defender])
            return
        self.attack(defender, attacker, stop=True)

    def handle_knockout(self, waifu: Waifu):
        log(f"{waifu.name} est KO")
        waifu.KO = True
        waifu.in_fight = False

        # Make the player or the npc choose a new waifu
        if len(self.player.get_alive_waifu()) == 0:
            print("Player à perdu, le NPC a gagné")
            self.finished = True
            return

        elif self.player.get_waifu_in_fight() is None:
            self.player.choice_next_waifu(waifu)
            return self.play_round(
                self.player.get_waifu_in_fight(), self.npc.get_waifu_in_fight()
            )

        if len(self.npc.get_alive_waifu()) == 0:
            print("NPC à perdu, le Player a gagné")
            self.finished = True
            return

        elif self.npc.get_waifu_in_fight() is None:
            self.npc.handle_choice_during_fight(self.player.get_waifu_in_fight(), waifu, True)
            return self.play_round(
                self.player.get_waifu_in_fight(), self.npc.get_waifu_in_fight()
            )


    def __get_multiplier(self, attacker: Waifu, move_used: Move, opponent: Waifu):
        if any(move_used.type.type_name == type.type_name for type in attacker.types):
            multiplier = 1.5
        else:
            multiplier = 1

        for type_ in opponent.types:
            if move_used.type.type_name in type_.immunities:
                log("C'est inefficace !")
                return 0
            
        for op_type in opponent.types:
            if move_used.type.type_name in op_type.weaknesses:
                log("C'est super efficace !")
                multiplier *= 2

        for op_type in opponent.types:
            if move_used.type.type_name in op_type.resistances:
                log("C'est pas très efficace...")
                multiplier /= 2

        if uniform(0, 100) <= 5.17:
            log("Coup critique !")
            multiplier *= 1.5

        return multiplier

    def calculate_damage(self, attacker: Waifu, opponent: Waifu):
        move_used = attacker.move_to_use
        if move_used.power == 0:
            return 0
        
        multiplier = self.__get_multiplier(attacker, move_used, opponent)
        damage = (
            ((2 * attacker.level + 10) / 250)
            * (attacker.attack / opponent.defense)
            * move_used.power
            + 2
        ) * multiplier

        return damage
