
def check_validity_of_input(pokemons, pokemon_name_dict):
    """
    Get input and check its validity. It has to be 6 different names with only one legendary pokemon in team
    """
    while True:
        names_of_pokemons = input("Choose 6 different names corresponding to the selected Pokemon "
                                  "and then write them down with a comma next to them without spaces. "
                                  "Note you can only have one legendary pokemon on your team: \n").split(',')
        names_of_pokemons = set(names_of_pokemons)
        numbers_of_pokemons = []
        if len(names_of_pokemons) == 6:
            for name in names_of_pokemons:
                if name in (pokemon_name_dict.values()):
                    numbers_of_pokemons.append(list(pokemon_name_dict.values()).index(name) + 1)
                else:
                    print(f"{name} is not valid pokemon name")
                    break
            if len(numbers_of_pokemons) == 6 and check_legendary_condition(numbers_of_pokemons, pokemons, pokemon_name_dict):
                return numbers_of_pokemons
        else:
            print("You didn't type six numbers")


def check_legendary_condition(pokemon_numbers, pokemons, pokemon_name_dict):
    """
    check legendary condition of the player, player has to choose only 1 legendary pokemon
    """
    legendary_pokemons = 0
    for number in pokemon_numbers:
        if pokemons[pokemon_name_dict[number]][-1] == "True":
            legendary_pokemons += 1
    if legendary_pokemons >= 2:
        print("\nYou have specified too many legendary pokemons. Try again: ")
        return False
    else:
        return True


def check_action_input(pokemons_in_hand):
    """
    check action input, input has to be integer value in range 1 to 5
    """
    while True:
        try:
            option = int(input(f"Choose 1 of 5 options: "))
        except ValueError:
            print(f"Please input integer value in range 1 to 5")
            continue
        if 0 < option < 6:
            if option != 4 or pokemons_in_hand > 0:
                return option
            else:
                print("You don't have any live pokemons")
        else:
            print("Value is out of range")


def check_replace_input(dict_of_pokemons):
    """
    check replace input, pokemon has to be on hand
    """
    while True:
        name = input("Write name of the new pokemon to fight: ")
        if name in (dict_of_pokemons.values()):
            return list(dict_of_pokemons.values()).index(name) + 1
        else:
            print("There is no such Pokemon on your hand")


def check_if_yes(player_num):
    """
    check if players are ready, if yes or y then start the battle
    """
    while True:
        decision = input(f"Player{player_num}: Write yes or y if you want to start the battle: ")
        if decision.lower() == "yes" or decision.lower() == "y":
            return True
        else:
            print("You didn't write yes/y")
