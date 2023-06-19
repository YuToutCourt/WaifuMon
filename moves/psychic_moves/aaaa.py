import os

def is_effect_empty(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        if "pass" in content and "power=0" in content:
            return True


def check_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                if is_effect_empty(file_path):
                    print(f"Le fichier '{file_path}' contient une fonction 'effect' vide.")
                    # os.remove(file_path)


# Exemple d'utilisation
directory_path = './'
check_directory(directory_path)
