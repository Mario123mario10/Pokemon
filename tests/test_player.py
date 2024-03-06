import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/src")
from player import Player
from pokemon import Pokemon

def test_player_init():
    pokemon1 = Pokemon("Bulbasaur" , 45, ["Grass", "Poison"], 49, 49, 65, 65, 45, False, False)
    pokemon2 = Pokemon("Ivysaur", 60, ["Grass", "Poison"], 62, 63, 80, 80, 60, False, False)
    pokemon3 = Pokemon("Charmeleon", 58, ["Fire", ""], 64, 58, 80, 65, 80, False, False)
    player1 = Player("Mario", [pokemon1], pokemon2, [pokemon3])
    assert player1.get_dead_pokemons() == [pokemon3]
    player1.set_dead_pokemons([pokemon2])
    assert player1.get_dead_pokemons() == [pokemon2]
    assert player1.get_active_pokemon() == pokemon2
    player1.set_active_pokemon(pokemon1)
    assert player1.get_active_pokemon() == pokemon1
    assert player1.get_name() == "Mario"
    player1.set_name("Siri")
    assert player1.get_name() == "Siri"
    assert player1.get_pokemons_in_hand() == [pokemon1]
    player1.set_pokemons_in_hand([pokemon2])
    assert player1.get_pokemons_in_hand() == [pokemon2]