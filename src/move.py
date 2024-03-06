from random import choice


class Move:
    """Class Move. Contains attributes
    param move_type: type of move, which can be normal or special
    type move_type: str

    param player1: attacking player
    type player1: object

    param player2: defending player
    type player2: object
    """
    def __init__(self, move_type, player1, player2):
        self._move_type = move_type
        self._player1 = player1
        self._player2 = player2

    def get_player1(self):
        """
        Returns player1 object
        """
        return self._player1

    def get_player2(self):
        """
        Returns player2 object
        """
        return self._player2


    def attack(self, weather):
        """
        It implements the logic associated with the Pokemon attack: it prints information about the health and burning of fighting Pokemon,
        calculates the damage inflicted and sets the health status of the oponent's pokemon
        """
        print(f'Health of your oponent before your attack was {self._player2.get_active_pokemon().get_health()}')
        damage = self._player1.get_active_pokemon().actual_damage(weather, self._player2.get_active_pokemon(), self._move_type)
        self._player2.get_active_pokemon().set_health(round(self._player2.get_active_pokemon().get_health() - damage, 2))
        if self.burn_enemy_pokemon():
            print(f"Your pokemon made {damage} damage and burn enemy pokemon")
            print(f"Health of your oponent after your attack is {self._player2.get_active_pokemon().get_health()}, and it's burning")
            self._player2.get_active_pokemon().set_burn(True)
        elif self._player2.get_active_pokemon().get_burn():
            print(f"Your pokemon made {damage} damage")
            print(f"Health of your oponent after your attack is {self._player2.get_active_pokemon().get_health()}, and it's burning")
        else:
            print(f"Your pokemon made {damage} damage")
            print(f'Health of your oponent after your attack is {self._player2.get_active_pokemon().get_health()}')
        if self._player2.get_active_pokemon().get_health() <= 0:
            print(f'{self._player2.get_active_pokemon().get_name()} is dead')
            self._player2.get_dead_pokemons().append(self._player2.get_active_pokemon())
            pokemon = self._player2.get_pokemons_in_hand().pop(0) if len(self._player2.get_pokemons_in_hand()) > 0 else None
            self._player2.set_active_pokemon(pokemon)
            print(f"Your new oponent is {pokemon.get_name()}\nStats of {pokemon.get_name()}: {pokemon}") if pokemon is not None else None


    def burn_enemy_pokemon(self):
        """
        Returns True when oponent's burning parameter was successful, else returns False.
        """
        if "Water" not in self._player2.get_active_pokemon().get_types():
            if "Fire" in self._player1.get_active_pokemon().get_types():
                pokemon_burn = choice([False, False, False, False, True])
                return pokemon_burn
        return False


    def increasing_special_defense_factor(self):
        """
        Increasing defense factor of actual pokemon.
        """
        print(f'Your last special defense was {self._player1.get_active_pokemon().get_special_defense()}')
        self._player1.get_active_pokemon().set_special_defense(round(self._player1.get_active_pokemon().get_special_defense() * 1.1, 2))
        print(f'Your special defence is now {self._player1.get_active_pokemon().get_special_defense()}')



    def replace_pokemon(self, chosen_pokemon, player):
        """
        Replaces the pokemon with the pokemon chosen by the player.
        """
        player.get_pokemons_in_hand().append(player.get_active_pokemon())
        player.get_pokemons_in_hand().remove(chosen_pokemon)
        player.set_active_pokemon(chosen_pokemon)