import os
from enum_moves import Moves

def is_effect_empty(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        if "pass" in content and "power=0" in content:
            return True


def check_directory():
    directory_path = os.path.join(os.getcwd()).replace("\\", "/")
    # get all the dir in the directory
    dirs = [dir for dir in os.listdir(directory_path) if os.path.isdir(dir)]

    for dir in dirs:
        if dir == "rock_moves" or dir == "steel_moves" or dir == "water_moves":
            files = os.listdir(dir)
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(directory_path, dir, file).replace("\\", "/")
                    if is_effect_empty(file_path):
                        print(f"Le fichier '{file_path}' contient une fonction 'effect' vide.")
                        os.remove(file_path)



def check_import():
    with open("move_factory.py", 'r') as files:
        content = files.read().split("\n")
        for line in content:
            if "from" in line:
                file_path = "/".join(line.split(" ")[1].split(".")[1:]) + ".py"
                if not os.path.isfile(file_path):
                    # remove the line from the file
                    content.remove(line)
                    print(f"Line '{line}' removed from 'move_factory.py'")

        with open("move_factory.py", 'w') as files:
            files.write("\n".join(content))

def get_number_enum(name, content):
    for line in content:
        if name in line:
            number = int(line.split("=")[-1].strip())
            return number


def check_enum():
    with open("enum_moves.py", 'r') as files:
        enum_file = files.read().split("\n")
    with open("move_factory.py", 'r') as files:
        content = files.read().split("\n")

    for move in Moves:
        found = False
        for line in content:
            if "from" in line:
                if move.name.lower() in line:
                    found = True
                    break
        if not found:
            print(f"Move '{move.name}' not found in 'move_factory.py'")
            name = f"    {move.name} = {get_number_enum(move.name, enum_file)}"
            print(f"Line '{name}' removed from 'enum_moves.py'")
            enum_file.remove(name)
            
        
    with open("enum_moves.py", 'w') as files:
        files.write("\n".join(enum_file))


check_directory()
check_import()
check_enum()