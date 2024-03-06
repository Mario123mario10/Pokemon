class Player:
    """Class Player. Contains attributes
    param name: player's name
    type name: str

    param pokemons_in_hand: Pokemons selected at the beginning of the game,
    currently not fighting, available for exchange for a fighting Pokemon
    type pokemons_in_hand: list of pokemons object

    param active pokemon: fighting pokemon
    type active_pokemon: Pokemon class

    param dead_pokemons: killed pokemons
    type dead_pokemons: list of pokemons object
    """
    def __init__(self, name, pokemons_in_hand, active_pokemon, dead_pokemons=None):
        self._name = name
        self._pokemons_in_hand = pokemons_in_hand
        self._active_pokemon = active_pokemon
        self._dead_pokemons = dead_pokemons if dead_pokemons is not None else []


    def get_dead_pokemons(self):
        """
        Returns dead pokemons
        """
        return self._dead_pokemons


    def set_dead_pokemons(self, dead_pokemons):
        """
        Set dead pokemons
        """
        self._dead_pokemons = dead_pokemons


    def get_active_pokemon(self):
        """
        Returns fighting pokemon
        """
        return self._active_pokemon


    def set_active_pokemon(self, pokemon):
        """
        Set active Pokemon
        """
        self._active_pokemon = pokemon


    def get_name(self):
        """
        Returns player's name
        """
        return self._name


    def set_name(self, name):
        """
        Changes player's name
        """
        self._name = name


    def get_pokemons_in_hand(self):
        """
        Returns pokemons in hand
        """
        return self._pokemons_in_hand

    def set_pokemons_in_hand(self, pokemons):
        """
        Set pokemons in hand
        """
        self._pokemons_in_hand = pokemons