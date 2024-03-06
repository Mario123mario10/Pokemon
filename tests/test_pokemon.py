import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/src")
from pokemon import Pokemon

def test_pokemon_init_and_print():
    pokemon1 = Pokemon("Bulbasaur" , 45, ["Grass", "Poison"], 49, 49, 65, 65, 45, False, False)
    assert pokemon1.get_name() == "Bulbasaur"
    assert pokemon1.get_health() == 45
    pokemon1.set_health(30)
    assert pokemon1.get_health() == 30
    assert pokemon1.get_defense() == 49
    pokemon1.set_defense(55)
    assert pokemon1.get_defense() == 55
    assert pokemon1.get_special_defense() == 65
    assert pokemon1.get_types() == ["Grass", "Poison"]
    assert pokemon1.get_burn() == False
    pokemon1.set_burn(True)
    assert pokemon1.get_burn() == True
    assert pokemon1.get_legendary() == False
    assert pokemon1.get_speed() == 45
    assert str(pokemon1) == ("name: Bulbasaur, health: 30, types: ['Grass', 'Poison'],\n"
    "attack: 49, defense: 55, special attack: 65, special defense: 65, "
    "speed: 45, legendary: False, burn: True")


def test_critical_damage(monkeypatch):
    def returnvalue(f):
        return 1.5
    pokemon1 = Pokemon("Bulbasaur" , 45, ["Grass", "Poison"], 49, 49, 65, 65, 45, False, False)
    monkeypatch.setattr('pokemon.choice', returnvalue)
    assert pokemon1.critical_damage() == 1.5

def test_attack_with_weather_without_bonus():
    pokemon1 = Pokemon("Bulbasaur" , 45, ["Grass", "Poison"], 49, 49, 65, 65, 45, False, False)
    pokemon1.attack_with_weather("rain") == 1

def test_attack_with_weather_with_water_bonus():
    pokemon1 = Pokemon("Bulbasaur" , 45, ["Water", "Poison"], 49, 49, 65, 65, 45, False, False)
    pokemon1.attack_with_weather("rain") == 1.5

def test_attack_with_weather_with_water_penalty():
    pokemon1 = Pokemon("Bulbasaur" , 45, ["Water", "Poison"], 49, 49, 65, 65, 45, False, False)
    pokemon1.attack_with_weather("harsch sunlight") == 0.5

def test_attack_with_weather_with_water_and_fire():
    pokemon1 = Pokemon("Bulbasaur" , 45, ["Water", "Fire"], 49, 49, 65, 65, 45, False, False)
    pokemon1.attack_with_weather("rain") == 1.5

def test_attack_without_the_same_type():
    pokemon1 = Pokemon("Bulbasaur" , 45, ["Water", "Fire"], 49, 49, 65, 65, 45, False, False)
    pokemon2 = Pokemon("Ivysaur", 60, ["Grass", "Poison"], 62, 63, 80, 80, 60, False, False)
    assert pokemon1.attack_with_same_type(pokemon2) == 1

def test_attack_with_the_same_type():
    pokemon1 = Pokemon("Bulbasaur" , 45, ["Poison", "Fire"], 49, 49, 65, 65, 45, False, False)
    pokemon2 = Pokemon("Ivysaur", 60, ["Grass", "Poison"], 62, 63, 80, 80, 60, False, False)
    assert pokemon1.attack_with_same_type(pokemon2) == 1.5

def test_attack_when_not_burn():
    pokemon1 = Pokemon("Bulbasaur" , 45, ["Poison", "Fire"], 49, 49, 65, 65, 45, False, False)
    pokemon1.get_burn() == 1

def test_attack_when_burn():
    pokemon1 = Pokemon("Bulbasaur" , 45, ["Poison", "Fire"], 49, 49, 65, 65, 45, False, True)
    pokemon1.get_burn() == 0.5

def test_type_ratio_2_types():
    pokemon1 = Pokemon("Bulbasaur" , 45, ["Water", ""], 49, 49, 65, 65, 45, False, False)
    pokemon2 = Pokemon("Ivysaur", 60, ["Grass", ""], 62, 63, 80, 80, 60, False, False)
    assert pokemon1.type_ratio(pokemon2) == 0.5

def test_type_ratio_4_types():
    pokemon1 = Pokemon("Bulbasaur" , 45, ["Water", "Fire"], 49, 49, 65, 65, 45, False, False)
    pokemon2 = Pokemon("Ivysaur", 60, ["Grass", "Poison"], 62, 63, 80, 80, 60, False, False)
    assert pokemon1.type_ratio(pokemon2) == 2

def test_actual_normal_damage(monkeypatch):
    def return220(j,k):
        return 220
    def return1(j):
        return 1
    pokemon1 = Pokemon("Ivysaur", 60, ["Grass", "Poison"], 62, 63, 80, 80, 60, False, False)
    pokemon2 = Pokemon("Charmeleon", 58, ["Fire", ""], 64, 58, 80, 65, 80, False, False)
    monkeypatch.setattr('pokemon.randint', return220)
    monkeypatch.setattr('pokemon.choice', return1)
    assert pokemon1.actual_damage("rain", pokemon2, "normal") == 3.11

def test_actual_special_damage(monkeypatch):
    def return220(j,k):
        return 220
    def return1(j):
        return 1
    pokemon1 = Pokemon("Ivysaur", 60, ["Grass", "Poison"], 62, 63, 80, 80, 60, False, False)
    pokemon2 = Pokemon("Charmeleon", 58, ["Fire", ""], 64, 58, 80, 65, 80, False, False)
    monkeypatch.setattr('pokemon.randint', return220)
    monkeypatch.setattr('pokemon.choice', return1)
    assert pokemon1.actual_damage("rain", pokemon2, "special") == 3.32