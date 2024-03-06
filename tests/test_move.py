import os
import sys
from copy import copy
from io import StringIO
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/src")
from pokemon import Pokemon
from player import Player
from move import Move



def test_suceeded_burn_enemy_pokemon(monkeypatch):
    def returnTrue(f):
        return True
    pokemon1 = Pokemon("Bulbasaur" , 45, ["Grass", "Poison"], 49, 49, 65, 65, 45, False, False)
    pokemon2 = Pokemon("Ivysaur", 60, ["Grass", "Poison"], 62, 63, 80, 80, 60, False, False)
    pokemon3 = Pokemon("Charmeleon", 58, ["Fire", ""], 64, 58, 80, 65, 80, False, False)
    player1 = Player("Mario", [pokemon1], pokemon3, [pokemon2])
    player2 = Player("Victoria", [copy(pokemon3)], copy(pokemon2), [copy(pokemon1)])
    move1 = Move("normal", player1, player2)
    monkeypatch.setattr('move.choice', returnTrue)
    assert move1.get_player2() == player2
    assert move1.burn_enemy_pokemon() is True

def test_impossible_to_burn_enemy_pokemon_for_water():
    pokemon1 = Pokemon("Bulbasaur" , 45, ["Grass", "Poison"], 49, 49, 65, 65, 45, False, False)
    pokemon2 = Pokemon("Ivysaur", 60, ["Water", "Poison"], 62, 63, 80, 80, 60, False, False)
    pokemon3 = Pokemon("Charmeleon", 58, ["Fire", ""], 64, 58, 80, 65, 80, False, False)
    player1 = Player("Mario", [pokemon1], pokemon3, [pokemon2])
    player2 = Player("Victoria", [copy(pokemon3)], copy(pokemon2), [copy(pokemon1)])
    move1 = Move("normal", player1, player2)
    assert move1.burn_enemy_pokemon() is False

def test_imposiible_to_burn_enemy_pokemon_for_not_fire():
    pokemon1 = Pokemon("Bulbasaur" , 45, ["Grass", "Poison"], 49, 49, 65, 65, 45, False, False)
    pokemon2 = Pokemon("Ivysaur", 60, ["Grass", "Poison"], 62, 63, 80, 80, 60, False, False)
    pokemon3 = Pokemon("Charmeleon", 58, ["Grass", ""], 64, 58, 80, 65, 80, False, False)
    player1 = Player("Mario", [pokemon1], pokemon3, [pokemon2])
    player2 = Player("Victoria", [copy(pokemon3)], copy(pokemon2), [copy(pokemon1)])
    move1 = Move("normal", player1, player2)
    assert move1.burn_enemy_pokemon() is False


def test_increasing_defense_factor():
    pokemon1 = Pokemon("Bulbasaur" , 45, ["Grass", "Poison"], 49, 49, 65, 65, 45, False, False)
    pokemon2 = Pokemon("Ivysaur", 60, ["Grass", "Poison"], 62, 63, 80, 80, 60, False, False)
    pokemon3 = Pokemon("Charmeleon", 58, ["Grass", ""], 64, 58, 80, 65, 80, False, False)
    player1 = Player("Mario", [pokemon1], pokemon3, [pokemon2])
    player2 = Player("Victoria", [copy(pokemon3)], copy(pokemon2), [copy(pokemon1)])
    move1 = Move("normal", player1, player2)
    move1.increasing_special_defense_factor()
    assert pokemon3.get_special_defense() == 71.5
    assert player2.get_pokemons_in_hand()[0].get_special_defense() == 65


def test_replace_pokemon():
    pokemon1 = Pokemon("Bulbasaur" , 45, ["Grass", "Poison"], 49, 49, 65, 65, 45, False, False)
    pokemon2 = Pokemon("Ivysaur", 60, ["Grass", "Poison"], 62, 63, 80, 80, 60, False, False)
    pokemon3 = Pokemon("Charmeleon", 58, ["Grass", ""], 64, 58, 80, 65, 80, False, False)
    player1 = Player("Mario", [pokemon1], pokemon3, [pokemon2])
    player2 = Player("Victoria", [copy(pokemon3)], copy(pokemon2), [copy(pokemon1)])
    move1 = Move("normal", player1, player2)
    move1.replace_pokemon(pokemon1, player1)
    assert player1.get_pokemons_in_hand() == [pokemon3]
    assert player1.get_active_pokemon() == pokemon1


def test_attack_move_without_burn_health_more_than_0(monkeypatch):
    def return220(j,k):
        return 220
    def return1(j):
        return 1
    pokemon1 = Pokemon("Bulbasaur" , 45, ["Grass", "Poison"], 49, 49, 65, 65, 45, False, False)
    pokemon2 = Pokemon("Ivysaur", 60, ["Grass", "Poison"], 62, 63, 80, 80, 60, False, False)
    pokemon3 = Pokemon("Charmeleon", 58, ["Fire", ""], 64, 58, 80, 65, 80, False, False)
    player1 = Player("Mario", [pokemon1], pokemon2, [pokemon3])
    player2 = Player("Mark", [copy(pokemon2)], copy(pokemon3), [copy(pokemon1)])
    move1 = Move("normal", player1, player2)
    monkeypatch.setattr('pokemon.randint', return220)
    monkeypatch.setattr('pokemon.choice', return1)
    output = StringIO()
    sys.stdout = output
    move1.attack("rain")
    sys.stdout = sys.__stdout__
    assert output.getvalue() == "Health of your oponent before your attack was 58\n\
Your pokemon made 3.11 damage\nHealth of your oponent after your attack is 54.89\n"

def test_attack_move_without_burn_health_less_than_0(monkeypatch):
    def return220(j,k):
        return 220
    def return1(j):
        return 1
    pokemon1 = Pokemon("Bulbasaur" , 45, ["Grass", "Poison"], 49, 49, 65, 65, 45, False, False)
    pokemon2 = Pokemon("Ivysaur", 60, ["Grass", "Poison"], 62, 63, 80, 80, 60, False, False)
    pokemon3 = Pokemon("Charmeleon", 1, ["Fire", ""], 64, 58, 80, 65, 80, False, False)
    player1 = Player("Mario", [pokemon1], pokemon2, [pokemon3])
    player2 = Player("Mark", [copy(pokemon2)], copy(pokemon3), [copy(pokemon1)])
    move1 = Move("normal", player1, player2)
    monkeypatch.setattr('pokemon.randint', return220)
    monkeypatch.setattr('pokemon.choice', return1)
    output = StringIO()
    sys.stdout = output
    move1.attack("rain")
    sys.stdout = sys.__stdout__
    assert output.getvalue() == "Health of your oponent before your attack was 1\n\
Your pokemon made 3.11 damage\nHealth of your oponent after your attack is -2.11\nCharmeleon is dead\n\
Your new oponent is Ivysaur\nStats of Ivysaur: name: Ivysaur, health: 60, types: \
['Grass', 'Poison'],\nattack: 62, defense: 63, special attack: 80, special defense: 80, speed: 60, legendary: False, burn: False\n"


def test_attack_move_with_attacker_arleady_burn(monkeypatch):
    def return220(j,k):
        return 220
    def return1(j):
        return 1
    pokemon1 = Pokemon("Bulbasaur" , 45, ["Grass", "Poison"], 49, 49, 65, 65, 45, False, False)
    pokemon2 = Pokemon("Ivysaur", 60, ["Grass", "Poison"], 62, 63, 80, 80, 60, False, True)
    pokemon3 = Pokemon("Charmeleon", 58, ["Fire", ""], 64, 58, 80, 65, 80, False, False)
    player1 = Player("Mario", [pokemon1], pokemon2, [pokemon3])
    player2 = Player("Mark", [copy(pokemon2)], copy(pokemon3), [copy(pokemon1)])
    move1 = Move("normal", player1, player2)
    monkeypatch.setattr('pokemon.randint', return220)
    monkeypatch.setattr('pokemon.choice', return1)
    output = StringIO()
    sys.stdout = output
    move1.attack("rain")
    sys.stdout = sys.__stdout__
    assert output.getvalue() == "Health of your oponent before your attack was 58\n\
Your pokemon made 2.18 damage\nHealth of your oponent after your attack is 55.82\n"



def test_attack_move_with_attacker_and_defender_arleady_burn(monkeypatch):
    def return220(j,k):
        return 220
    def return1(j):
        return 1
    pokemon1 = Pokemon("Bulbasaur" , 45, ["Grass", "Poison"], 49, 49, 65, 65, 45, False, False)
    pokemon2 = Pokemon("Ivysaur", 60, ["Grass", "Poison"], 62, 63, 80, 80, 60, False, True)
    pokemon3 = Pokemon("Charmeleon", 58, ["Fire", ""], 64, 58, 80, 65, 80, False, True)
    player1 = Player("Mario", [pokemon1], pokemon2, [pokemon3])
    player2 = Player("Mark", [copy(pokemon2)], copy(pokemon3), [copy(pokemon1)])
    move1 = Move("normal", player1, player2)
    monkeypatch.setattr('pokemon.randint', return220)
    monkeypatch.setattr('pokemon.choice', return1)
    output = StringIO()
    sys.stdout = output
    move1.attack("rain")
    sys.stdout = sys.__stdout__
    assert output.getvalue() == "Health of your oponent before your attack was 58\n\
Your pokemon made 2.18 damage\nHealth of your oponent after your attack is 55.82, and it's burning\n"

def test_attack_move_burning_enemy_pokemon(monkeypatch):
    def return220(j,k):
        return 220
    def return1(j):
        return 1
    def returnTrue(j):
        return True
    pokemon1 = Pokemon("Bulbasaur" , 45, ["Grass", "Poison"], 49, 49, 65, 65, 45, False, False)
    pokemon2 = Pokemon("Ivysaur", 60, ["Fire", "Poison"], 62, 63, 80, 80, 60, False, True)
    pokemon3 = Pokemon("Charmeleon", 58, ["Fire", ""], 64, 58, 80, 65, 80, False, False)
    player1 = Player("Mario", [pokemon1], pokemon2, [pokemon3])
    player2 = Player("Mark", [copy(pokemon2)], copy(pokemon3), [copy(pokemon1)])
    move1 = Move("normal", player1, player2)
    monkeypatch.setattr('pokemon.randint', return220)
    monkeypatch.setattr('pokemon.choice', return1)
    monkeypatch.setattr('move.choice', returnTrue)
    output = StringIO()
    sys.stdout = output
    move1.attack("rain")
    sys.stdout = sys.__stdout__
    assert output.getvalue() == "Health of your oponent before your attack was 58\n\
Your pokemon made 1.63 damage and burn enemy pokemon\nHealth of your oponent after your attack is 56.37, and it's burning\n"
    assert player2.get_active_pokemon().get_burn() == True

def test_attack_move_burning_enemy_pokemon_when_its_burning(monkeypatch):
    def return220(j,k):
        return 220
    def return1(j):
        return 1
    def returnTrue(j):
        return True
    pokemon1 = Pokemon("Bulbasaur" , 45, ["Grass", "Poison"], 49, 49, 65, 65, 45, False, False)
    pokemon2 = Pokemon("Ivysaur", 60, ["Fire", "Poison"], 62, 63, 80, 80, 60, False, True)
    pokemon3 = Pokemon("Charmeleon", 58, ["Fire", ""], 64, 58, 80, 65, 80, False, True)
    player1 = Player("Mario", [pokemon1], pokemon2, [pokemon3])
    player2 = Player("Mark", [copy(pokemon2)], copy(pokemon3), [copy(pokemon1)])
    move1 = Move("normal", player1, player2)
    monkeypatch.setattr('pokemon.randint', return220)
    monkeypatch.setattr('pokemon.choice', return1)
    monkeypatch.setattr('move.choice', returnTrue)
    output = StringIO()
    sys.stdout = output
    move1.attack("rain")
    sys.stdout = sys.__stdout__
    assert output.getvalue() == "Health of your oponent before your attack was 58\n\
Your pokemon made 1.63 damage and burn enemy pokemon\nHealth of your oponent after your attack is 56.37, and it's burning\n"


def test_attack_move_impossible_burning_because_of_water(monkeypatch):
    def return220(j,k):
        return 220
    def return1(j):
        return 1
    def returnTrue(j):
        return True
    pokemon1 = Pokemon("Bulbasaur" , 45, ["Grass", "Poison"], 49, 49, 65, 65, 45, False, False)
    pokemon2 = Pokemon("Ivysaur", 60, ["Fire", "Poison"], 62, 63, 80, 80, 60, False, False)
    pokemon3 = Pokemon("Charmeleon", 58, ["Water", ""], 64, 58, 80, 65, 80, False, False)
    player1 = Player("Mario", [pokemon1], pokemon2, [pokemon3])
    player2 = Player("Mark", [copy(pokemon2)], copy(pokemon3), [copy(pokemon1)])
    move1 = Move("normal", player1, player2)
    monkeypatch.setattr('pokemon.randint', return220)
    monkeypatch.setattr('pokemon.choice', return1)
    monkeypatch.setattr('move.choice', returnTrue)
    output = StringIO()
    sys.stdout = output
    move1.attack("rain")
    sys.stdout = sys.__stdout__
    assert output.getvalue() == "Health of your oponent before your attack was 58\n\
Your pokemon made 1.55 damage\nHealth of your oponent after your attack is 56.45\n"


def test_attack_move_burning_enemy_pokemon_when_health_less_than_0(monkeypatch):
    def return220(j,k):
        return 220
    def return1(j):
        return 1
    def returnTrue(j):
        return True
    pokemon1 = Pokemon("Bulbasaur" , 45, ["Grass", "Poison"], 49, 49, 65, 65, 45, False, False)
    pokemon2 = Pokemon("Ivysaur", 60, ["Fire", "Poison"], 62, 63, 80, 80, 60, False, True)
    pokemon3 = Pokemon("Charmeleon", 0.5, ["Fire", ""], 64, 58, 80, 65, 80, False, False)
    pokemon4 = Pokemon("Ivysaur", 60, ["Fire", "Poison"], 62, 63, 80, 80, 60, False, False)
    player1 = Player("Mario", [pokemon1], pokemon2, [pokemon3])
    player2 = Player("Mark", [copy(pokemon4)], copy(pokemon3), [copy(pokemon1)])
    move1 = Move("normal", player1, player2)
    monkeypatch.setattr('pokemon.randint', return220)
    monkeypatch.setattr('pokemon.choice', return1)
    monkeypatch.setattr('move.choice', returnTrue)
    output = StringIO()
    sys.stdout = output
    move1.attack("rain")
    sys.stdout = sys.__stdout__
    assert player2.get_dead_pokemons()[-1].get_burn() == True
    assert output.getvalue() == "Health of your oponent before your attack was 0.5\n\
Your pokemon made 1.63 damage and burn enemy pokemon\nHealth of your oponent after your attack is -1.13, and it's burning\nCharmeleon is dead\n\
Your new oponent is Ivysaur\nStats of Ivysaur: name: Ivysaur, health: 60, types: \
['Fire', 'Poison'],\nattack: 62, defense: 63, special attack: 80, special defense: 80, speed: 60, legendary: False, burn: False\n"