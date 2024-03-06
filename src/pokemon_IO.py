import requests
import csv

csv_url = "https://gist.githubusercontent.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6/raw/92200bc0a673d5ce2110aaad4544ed6c4010f687/pokemon.csv"

def get_pokemon_csv():
    """
    Returns dictionary from csv_url path, when the keys are names of pokemons and values are attributes of pokemons.
    """
    with requests.get(csv_url, stream = True) as r:
        lines = (line.decode("UTF-8") for line in r.iter_lines())
        pokemon_dict = {}
        reader = csv.reader(lines)
        next(reader, None)
        for line in reader:
            pokemon_dict[line[1]] = line[2:]
        return pokemon_dict