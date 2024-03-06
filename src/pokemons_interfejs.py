from player import Player
from pokemon import Pokemon
from pokemon_IO import get_pokemon_csv
from move import Move
from arena import Arena
from random import choice
import inputs_validators as iv


def is_end(move, player1, player2):
    if move.get_player2().get_active_pokemon() is None:
        if move.get_player1() is player1:
            print(f'\n================<Player 1, {player1.get_name()} win>================')
        else:
            print(f'\n================<Player 2, {player2.get_name()} win>================')
        return True
    return False


def setup_game():
    name1 = input("Player1: Write your name: ")
    name2 = input("Player2: Write your name: ")
    start_command1 = iv.check_if_yes(1)
    start_command2 = iv.check_if_yes(2)
    if start_command1 and start_command2:
        pokemons = get_pokemon_csv()
        pokemon_name_dict = {index: name for index, name in enumerate(pokemons.keys(), start=1)}
        pokemon_name_dict_legens = {index: "-##(L)##" if value[10] == "True" else "" for index, (name, value) in
                                    enumerate(pokemons.items(), start=1)}
        final_pokemon_dict = dict([(k, pokemon_name_dict[k] + pokemon_name_dict_legens[k]) for k in pokemon_name_dict])
        list_of_pokemons1 = []
        list_of_pokemons2 = []
        for i in range(0, 2):
            print(final_pokemon_dict)
            print(f"\n===============PLAYER {i + 1} TURN ==================\n")
            pokemon_numbers = iv.check_validity_of_input(pokemons, pokemon_name_dict)
            for number in pokemon_numbers:
                attributes = pokemons[pokemon_name_dict[number]]
                if i == 0:
                    list_of_pokemons1.append(Pokemon(pokemon_name_dict[int(number)], int(attributes[3]),
                                                     attributes[0:2], int(attributes[4]), int(attributes[5]),
                                                     int(attributes[6]), int(attributes[7]), int(attributes[8]),
                                                     attributes[10], False))
                else:
                    list_of_pokemons2.append(Pokemon(pokemon_name_dict[int(number)], int(attributes[3]),
                                                     attributes[0:2], int(attributes[4]), int(attributes[5]),
                                                     int(attributes[6]), int(attributes[7]), int(attributes[8]),
                                                     attributes[10], False))

        player1 = Player(name1, list_of_pokemons1[1:], list_of_pokemons1[0])
        player2 = Player(name2, list_of_pokemons2[1:], list_of_pokemons2[0])
        arena = Arena(player1, player2)
        return arena


def choose_starter(player1, player2):
    if player1.get_active_pokemon().get_speed() > player2.get_active_pokemon().get_speed():
        print("\n================<PLAYER 1 TURN>================")
        attacker = player1
        defender = player2
    elif player1.get_active_pokemon().get_speed() < player2.get_active_pokemon().get_speed():
        print("\n================<PLAYER 2 TURN>================")
        attacker = player2
        defender = player1
    else:
        value = choice([1, 2])
        if value == 1:
            print("\n================<PLAYER 1 TURN>================")
            attacker = player1
            defender = player2
        else:
            print("\n================<PLAYER 2 TURN>================")
            attacker = player2
            defender = player1
    return attacker, defender


def gameplay(attacker, defender, player1, player2, arena):
    number_of_turns = 1
    rounds = 0
    end_flag = False
    while not end_flag:
        if number_of_turns % 2 == 1:
            rounds += 1
            arena.pick_weather()
            weather = arena.get_weather()
        print(f"===================<ROUND {rounds}>===================")
        print(f"Weather: {weather}")
        print(f"Stats of YOUR pokemon: {attacker.get_active_pokemon()}")
        print(f"Stats of ENEMY pokemon: {defender.get_active_pokemon()}\n")
        print("1.normal attack, 2.special attack, 3.increasing special defense factor, 4.replace pokemon, 5.surrender")
        option = iv.check_action_input(len(attacker.get_pokemons_in_hand()))
        if option == 1:
            move = Move("normal", attacker, defender)
            move.attack(arena.get_weather())
            end_flag = is_end(move, player1, player2)
        if option == 2:
            move = Move("special", attacker, defender)
            move.attack(arena.get_weather())
            end_flag = is_end(move, player1, player2)
        if option == 3:
            move = Move("defense", attacker, defender)
            move.increasing_special_defense_factor()
        if option == 4:
            move = Move("replace", attacker, defender)
            list_of_names = [pokemon.get_name() for pokemon in attacker.get_pokemons_in_hand()]
            pokemon_name_dict = {index: name for index, name in enumerate(list_of_names, start=1)}
            print(f'\n{pokemon_name_dict}')
            number = iv.check_replace_input(pokemon_name_dict)
            move.replace_pokemon(attacker.get_pokemons_in_hand()[number - 1], attacker)
        if option == 5:
            end_flag = True
            print(f"{attacker.get_name()} surrendered")

        if attacker is player1 and end_flag == False:
            print("\n================<PLAYER 2 TURN>================")
            attacker = player2
            defender = player1
        elif attacker is player2 and end_flag == False:
            print("\n================<PLAYER 1 TURN>================")
            attacker = player1
            defender = player2
        number_of_turns += 1


def game(arena):
    """
    Function responsible for setting game and gameplay
    """
    player1 = arena.get_player1()
    player2 = arena.get_player2()

    print("\n=======================<BATTLE IS STARTED>=======================")
    attacker, defender = choose_starter(player1, player2)
    gameplay(attacker, defender, player1, player2, arena)


if __name__ == "__main__":
    arena = setup_game()
    game(arena)
