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
        self.turn = 0
        self.finished = False

    def start(self):
        """
        Start the fight
        """
        waifu_player = self.player.team[0] # Start with the first waifu of the player
        waifu_enemy = self.npc.team[0] # Start with the first waifu of the npc

        waifu_player.in_fight = True # Set the waifu in fight
        waifu_enemy.in_fight = True # Set the waifu in fight

        self.play_round(waifu_player, waifu_enemy) # Start the round

    def __check_team_waifu(self, waifu) -> Union[Player, NPC]:
        """
        Check in which team the waifu is
        :param waifu: Waifu to check
        :return: Player or NPC
        """
        for waifu_player in self.player.team: # Check in the player team
            if waifu_player == waifu:
                return self.player
        
        for waifu_npc in self.npc.team: # Check in the npc team
            if waifu_npc == waifu:
                return self.npc
            
        raise Exception("Waifu not found in team")
        
    def __apply_status_before_attack(self, waifu:Waifu):
        """
        Apply the status before the attack
        :param waifu: Waifu to check
        :return: True if the waifu can attack, False otherwise
        """
        if waifu.status is not None and waifu.status.after_attack == False:
            return waifu.status.apply_status()
        return True

    def __apply_status_after_attack(self, waifus:List[Waifu]):
        """
        Apply the status after the attack
        :param waifus: List of waifus
        """
        for waifu in waifus:
            if waifu.status is not None and waifu.status.after_attack:
                waifu.status.apply_status()

    def  __user_choice(self, waifu1, waifu2):
        """
        User choice
        The user can either attack, change waifu or capture the waifu
        :param waifu1: Waifu of the player (always)
        :param waifu2: Waifu of the NPC (always)
        :return: Waifu attacking and the choice of the player
        """
        choice = input_int("Que voulez vous faire ?\n1. Attaquer\n2. Changer de waifu\n3. Capturer la waifu\n", 1, 3) #TODO: Add the possibility to use an item
        if choice == 1: # If the player decides to attack, return the wafu1 attacking and "attack"
            return waifu1, "attack"
        elif choice == 2: # If the player decides to switch,  return waifu to switch to and "switch"
            return self.player.choice_next_waifu(waifu1), "switch"
        else: # If the player decides to capture, try to capture the waifu
            if len(self.player.team) >= 6: # If the team is full, the player can't capture the waifu TODO: Add the possibility to send a waifu to the box   
                print("Votre equipe est pleine, vous ne pouvez pas capturer de waifu")
                return self.__user_choice(waifu1, waifu2) # The player has to choose again
            if waifu2.get_owner() == "npc": # If the waifu is already owned, the player can't capture it
                print("Vous ne pouvez pas capturer la waifu d'un autre joueur")
                return self.__user_choice(waifu1, waifu2) # The player has to choose again
            else: # If the player can capture the waifu, try to capture it
                return waifu1, "capture" # Return the waifu attacking and "capture"

    def play_round(self, waifu1: Waifu, waifu2: Waifu):
        """
        Play a round of the fight
        :param waifu1: Waifu of the player (always)
        :param waifu2: Waifu of the NPC (always)
        """
        if self.finished: return # If the fight is finished, stop the fight
        self.__apply_status_after_attack([waifu1, waifu2]) # Apply the status after the attack
        log("Tour", self.turn) 
        log("Current battle", f"{waifu1.name} vs {waifu2.name}")
        self.turn += 1 # Increment the turn

        obj = self.__check_team_waifu(waifu1) # Check in which team the waifu is

        if isinstance(obj, Player):
            # Display the stats of the waifus
            waifu1.display_hp()    
            waifu1.display_stats()
            waifu2.display_hp()
            waifu2.display_stats()
            waifu1, choice  = self.__user_choice(waifu1, waifu2)  # The player chooses his action
            if choice == "attack":
                waifu1.choice_move() # If the player attack, he choose a move
            elif choice == "capture":
                capture_success = capture_waifu(waifu1, waifu2)
                if capture_success: # If the capture is a success, the fight is over
                    return
                waifu1.move_to_use = MoveFactory.create_move(Moves.NOTHING) # If the capture failed, the player can't attack
            elif choice == "switch":
                waifu1.move_to_use = MoveFactory.create_move(Moves.NOTHING) # If the player switch, he can't attack

            self.user_turn = False # The player has finished his turn

            waifu2, as_switch = self.npc.handle_choice_during_fight(waifu1, waifu2) # The npc chooses his action

            if as_switch: # If the npc switch, he can't attack
                waifu2.move_to_use = MoveFactory.create_move(Moves.NOTHING)

        else:
            # Display the stats of the waifus
            waifu2.display_hp()
            waifu2.display_stats()
            waifu1.display_hp()
            waifu1.display_stats()
            waifu2, choice = self.__user_choice(waifu2, waifu1)
            if choice == "attack":
                waifu2.choice_move() # If the player attack, he choose a move
            elif choice == "capture":
                capture_success = capture_waifu(waifu2, waifu1)
                if capture_success: # If the capture is a success, the fight is over
                    return
                waifu2.move_to_use = MoveFactory.create_move(Moves.NOTHING) # If the capture failed, the player can't attack
            elif choice == "switch":
                waifu2.move_to_use = MoveFactory.create_move(Moves.NOTHING) # If the player switch, he can't attack
            
            self.user_turn = False # The player has finished his turn

            waifu1, as_switch = self.npc.handle_choice_during_fight(waifu2, waifu1) # The npc chooses his action

            if as_switch: # If the npc switch, he can't attack
                waifu1.move_to_use = MoveFactory.create_move(Moves.NOTHING)

        attacking_waifu, defending_waifu = self.determine_attack_order(waifu1, waifu2) # Determine the order of the attack

        self.attack(attacking_waifu, defending_waifu) # Attack phase

        if defending_waifu.hp <= 0: # If the defending waifu is KO, the fight is over
            self.handle_knockout(defending_waifu)
            if attacking_waifu.hp <= 0:
                self.handle_knockout(attacking_waifu)
            return
        
        if attacking_waifu.hp <= 0: # If the attacking waifu is KO, the fight is over
            self.handle_knockout(attacking_waifu)
            return

        self.play_round(attacking_waifu, defending_waifu) # Next round

    def determine_attack_order(self, waifu1: Waifu, waifu2: Waifu):
        """
        Determine the order of the attack
        :param waifu1: Waifu of the player (always)
        :param waifu2: Waifu of the NPC (always)
        :return: attack order
        """
        if waifu1.move_to_use.priority == waifu2.move_to_use.priority: # If the priority of the moves are the same, the fastest waifu attack first
            return sorted([waifu1, waifu2], key=lambda waifu: waifu.speed, reverse=True)

        return sorted( # Else, the waifu with the highest priority attack first
            [waifu1, waifu2], key=lambda waifu: waifu.move_to_use.priority, reverse=True
        )

    def move_effect(self, attacker, defender, move_used):
        """
        Apply the effect of the move
        :param attacker: Attacking waifu (always)
        :param defender: Defending waifu (always)
        :param move_used: Move used
        """
        if randint(0, 100) <= move_used.proba_effect: # If the move has an effect, apply it
            # The try/except is here to handle moves that don't have an effect 
            # (because I don't wont to modify all the moves)
            try:
                attacker.move_to_use.effect(attacker, defender) # Apply the effect
                if defender.hp <= 0: # If the defending waifu is KO, the fight is over
                    defender.display_hp() # Display the hp of the waifu
                    return self.handle_knockout(defender) # Handle the KO
                if attacker.hp <= 0: # If the attacking waifu is KO, the fight is over
                    attacker.display_hp() # Display the hp of the waifu
                    return self.handle_knockout(attacker) # Handle the KO
            except Exception as e: 
                log("Effect Error ", e)

    def attack(self, attacker: Waifu, defender: Waifu, stop=False):
        """
        Attack phase
        :param attacker: Attacking waifu (always)
        :param defender: Defending waifu (always)
        :param stop: If True, the attack is the last of the turn
        """
        move_used = attacker.move_to_use # Move used by the attacking waifu
        log("Attack", f"{attacker.name} use {move_used.name}")
        if self.__apply_status_before_attack(attacker):
            if randint(0, 100) <= move_used.accuracy:  # If the move touch the defending waifu
                damage = self.calculate_damage(attacker, defender) # Calculate the damage
                animation_damage(defender, damage) # Display the animation of the damage
                log(move_used.name, f"{defender.name} a perdu {damage} PV")
                self.move_effect(attacker, defender, move_used) # Apply the effect of the move
                if defender.hp <= 0: # If the defending waifu is KO, the fight is over
                    defender.display_hp() # Display the hp of the waifu
                    return self.handle_knockout(defender) # Handle the KO
                

                if attacker.hp <= 0: # If the attacking waifu is KO, the fight is over
                    attacker.display_hp() # Display the hp of the waifu
                    return self.handle_knockout(attacker) # Handle the KO
                
                if defender.hp <= 0: # If the defending waifu is KO, the fight is over
                    defender.display_hp() # Display the hp of the waifu
                    return self.handle_knockout(defender) # Handle the KO
                
            else: # If the move doesn't touch the defending waifu
                print("Le coup n'a pas touché")


            if stop: # If the attack is the last of the turn, apply the status after the attack
                self.__apply_status_after_attack([attacker, defender]) 
                return  
        self.attack(defender, attacker, stop=True) # Else, the defending waifu attack

    def handle_knockout(self, waifu_ko: Waifu):
        """
        Handle the KO of a waifu
        :param waifu_ko: KO Waifu
        :param end_turn: If True, the KO is the last of the turn
        """
        log(f"{waifu_ko.name} est KO")
        waifu_ko.KO = True  # Set the waifu KO
        waifu_ko.in_fight = False # Set the waifu out of fight
        waifu_ko.status = None # Remove the status of the waifu
            
        # Make the player or the npc choose a new waifu
        if len(self.player.get_alive_waifu()) == 0: # If the player has no waifu alive, the fight is over
            print("Player à perdu, le NPC a gagné")
            self.finished = True 
            return 

        elif self.player.get_waifu_in_fight() is None: # If the player has no waifu in fight, the player has to choose a new waifu
            self.player.choice_next_waifu(waifu_ko) # The player chooses a new waifu
            return self.play_round( 
                self.player.get_waifu_in_fight(), self.npc.get_waifu_in_fight()
            )

        if len(self.npc.get_alive_waifu()) == 0: # If the npc has no waifu alive, the fight is over
            print("NPC à perdu, le Player a gagné")
            self.finished = True
            return

        elif self.npc.get_waifu_in_fight() is None: # If the npc has no waifu in fight, the npc has to choose a new waifu
            self.npc.handle_choice_during_fight(self.player.get_waifu_in_fight(), waifu_ko, True) # The npc chooses a new waifu
            return self.play_round( 
                self.player.get_waifu_in_fight(), self.npc.get_waifu_in_fight()
            )
            
        return 


    def __get_multiplier(self, attacker: Waifu, move_used: Move, opponent: Waifu):
        """
        Get the multiplier of the attack
        :param attacker: Attacking waifu (always)
        :param move_used: Move used
        :param opponent: Defending waifu (always)
        :return: Multiplier of the attack
        """
        if any(move_used.type.type_name == type.type_name for type in attacker.types): # If the attacking waifu has the same type as the move, the multiplier is 1.5
            multiplier = 1.5 
        else: # Else, the multiplier is 1
            multiplier = 1

        for type_ in opponent.types: # Check the type of the defending waifu
            log(type_.immunities, move_used.type.type_name) 
            if move_used.type.type_name in type_.immunities: # If the move is ineffective, the multiplier is 0
                log("C'est inefficace !")
                return 0
            
        for op_type in opponent.types: # Check the type of the defending waifu
            if move_used.type.type_name in op_type.weaknesses: # If the move is super effective, the multiplier is 2
                log("C'est super efficace !")
                multiplier *= 2

        for op_type in opponent.types: # Check the type of the defending waifu
            if move_used.type.type_name in op_type.resistances: # If the move is not very effective, the multiplier is 0.5
                log("C'est pas très efficace...")
                multiplier /= 2 

        if uniform(0, 100) <= 5.17: # If the move is a critical hit, the multiplier is 1.5
            log("Coup critique !")
            multiplier *= 1.5

        return multiplier

    def calculate_damage(self, attacker: Waifu, opponent: Waifu):
        """
        Calculate the damage of the attack
        :param attacker: Attacking waifu (always)
        :param opponent: Defending waifu (always)
        :return: Damage of the attack
        """
        move_used = attacker.move_to_use # Move used by the attacking waifu
        if move_used.power == 0: # If the move has no power, the damage is 0
            return 0
        
        multiplier = self.__get_multiplier(attacker, move_used, opponent) # Get the multiplier of the attack
        damage = ( # Calculate the damage
            ((2 * attacker.level + 10) / 250)
            * (attacker.attack / opponent.defense)
            * move_used.power
            + 2
        ) * multiplier

        return damage

def capture_waifu(self, waifu: Waifu):
        """
        Capture a the waifu of the opponent
        :param waifu: Waifu to capture
        :return: True if the capture is a success, False otherwise
        """
        if randint(0, 100) <= (waifu.hp / waifu.max_hp) * 100: # The capture is more likely to succeed if the waifu is low hp TODO: Add pokemon status to modify the capture rate
            print("Vous avez capturé la waifu !")
            print("Vous pouvez maintenant lui donner un nom") #TODO: Add the possibility to give a name to the waifu
            print("La waifu a rejoint votre équipe")
            waifu.owner = "player" # Modify the owner of the waifu
            self.player.team.append(waifu) # Add the waifu to the team
            return True # The capture is a success
        else:
            print("La waifu s'est échappé")
            return False # The capture is a failure