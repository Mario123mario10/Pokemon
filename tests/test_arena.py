import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/src")
from arena import Arena
from player import Player
from pokemon import Pokemon

def test_create_arena(monkeypatch):
    def returnrain(t):
        return "rain"
    Pokemon1 = Pokemon("Bulbasaur" , 45, ["Grass", "Poison"], 49, 49, 65, 65, 45, False, False)
    Pokemon2 = Pokemon("Ivysaur", 60, ["Grass", "Poison"], 62, 63, 80, 80, 60, False, False)
    Pokemon3 = Pokemon("Charmeleon", 58, ["Fire", ""], 64, 58, 80, 65, 80, False, False)
    player1 = Player("Mario", Pokemon1, Pokemon2, Pokemon3)
    player2 = Player("Victoria", Pokemon2, Pokemon3, Pokemon1)
    arena1 = Arena(player1, player2)
    monkeypatch.setattr('arena.choice', returnrain)
    assert arena1.get_weather() is None
    arena1.pick_weather()
    assert arena1.get_weather() == "rain"