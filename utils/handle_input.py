def input_int(txt, min_val=1, max_val=1000000000000):
    """
    Fonction pour choisir un nombre positif avec une gestion d'erreur
    :param txt: int, Le texte à afficher
    :param min_val: int, La valeur minimale
    :param max_val: int, La valeur maximale

    :return: int, Le nombre choisi
    """
    while True:
        number = input(txt)
        if number.isdigit() == False:
            print("Vous devez choisir un nombre !")
            continue
        number = int(number)
        # Vérifiez si le nombre est dans la plage spécifiée
        if min_val <= number <= max_val:
            return number
        elif number < min_val:
            print(f"Vous devez choisir un nombre supérieur ou égale à {min_val}")
        else:
            print(f"Vous devez choisir un nombre inférieur ou égale à {max_val}")
