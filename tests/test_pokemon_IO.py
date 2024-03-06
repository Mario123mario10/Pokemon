import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/src")
from pokemon_IO import get_pokemon_csv


def test_get_pokemon_csv():
    pokemon_dict = get_pokemon_csv()
    assert len(pokemon_dict) == 800
    assert "Wartortle" in pokemon_dict.keys()
    assert pokemon_dict["Wartortle"] == ['Water', '', '405', '59', '63', '80', '65', '80', '58', '1', 'False']