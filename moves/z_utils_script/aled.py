import os
from tqdm import tqdm

# from moves.move import Move
# from moves.enum_moves import Moves

current_path = os.getcwd()

import_attacks = []
file_name = []
class_files = []
# List all the dir in the current path
for dir in tqdm(os.listdir(current_path)):

    if dir.endswith(".py") or dir == "z_utils_script" or \
    dir == "__pycache__": continue

    if  dir == "status_moves" or dir == "stat_modifier_moves":
        
        for dir2 in tqdm(os.listdir(current_path + "\\" + dir)):
            if dir2.endswith(".py"): continue

            for file in os.listdir(current_path + "\\" + dir + "\\" + dir2):
                
                name_file = file.split(".")[0]

                # read the file
                with open(current_path + "\\" + dir + "\\" + dir2 + "\\" + file, "r") as f:
                    lines = f.readlines()

                    # find the class name
                    for line in lines:
                        if "class" in line:
                            class_file = line.split(" ")[1].split("(")[0]

                class_files.append(class_file)
                import_attacks.append(f"from moves.{dir}.{dir2}.{name_file} import {class_file}")
                file_name.append(name_file)


    else:
        # List all the files in the dir
        for file in os.listdir(current_path + "\\" + dir):
            
            name_file = file.split(".")[0]

            # read the file
            with open(current_path + "\\" + dir + "\\" + file, "r") as f:
                lines = f.readlines()

                # find the class name
                for line in lines:
                    if "class" in line:
                        class_file = line.split(" ")[1].split("(")[0]

            class_files.append(class_file)
            import_attacks.append(f"from moves.{dir}.{name_file} import {class_file}")
            file_name.append(name_file)

with open("./move_factory.py", "w") as f:
    for line in tqdm(import_attacks):
        f.write(line + "\n")

    f.write("\n\n")
    f.write("class MoveFactory:\n")
    f.write("    @staticmethod\n")
    f.write("    def create_move(move: Moves) -> Move:\n")
    f.write("        if isinstance(move, str):\n")
    f.write("            move = Moves[move.upper()]\n\n")
    f.write("        if move == Moves.ATTACK_ORDER:\n")
    f.write("            return AttackOrder()\n")
    for index_class, line in enumerate(file_name[1:]):
        f.write(f"        elif move == Moves.{line.upper()}:\n")
        f.write(f"            return {class_files[index_class]}()\n")

with open("./enum_moves.py", "w") as f:
    f.write("from enum import Enum\n\n")
    f.write("class Moves(Enum):\n")
    for index, line in tqdm(enumerate(file_name)):
        f.write(f"    {line.upper()} = {index + 1}\n")
