from random import randint, choice
import types_ratio_file


class Pokemon:
    """Class Pokemon. Contains attributes
    :param name: name of the pokemon
    :type name: str

    :param health: current health of the pokemon
    :type health: int

    :param types: list of types of pokemon, each pokemon can have 1 or 2 types
    :type types: list

    :param attack: constant attack rate of the pokemon
    :type attack: int

    :param defense: constant defense rate of the pokemon
    :type defense: int

    :param special_attack: constant special attack rate of the pokemon, usually stronger than attack rate
    :type special_attack: int

    :param special defense: constant special defense rate of the pokemon, usually stronger than defense rate
    :type special defense: int

    :param speed: speed of the pokemon, higher speed allows to begin the match first and have an advantage from the start
    :type speed: int

    :param legendary: this indicates whether the pokemon is legendary or not
    :type legendary: boolean

    :param burn: this indicates whether the pokemon is burning
    :type burn: boolean
    """
    def __init__(self, name, health, types, attack, defense, special_attack, special_defense, speed, legendary, burn):
        self._name = name
        self._health = health
        self._types = types
        self._attack = attack
        self._defense = defense
        self._burn = burn
        self._special_attack = special_attack
        self._special_defense = special_defense
        self._legendary = legendary
        self._speed = speed

    def get_name(self):
        """
        Returns name of the pokemon
        """
        return self._name

    def get_health(self):
        """
        Returns health of the pokemon
        """
        return self._health

    def set_health(self, health):
        """
        Set health for the pokemon
        """
        self._health = health

    def get_defense(self):
        """
        Returns defense of the pokemon
        """
        return self._defense

    def set_defense(self, defense):
        """
        Set defense of the pokemon
        """
        self._defense = defense

    def get_special_defense(self):
        """
        Returns special defense of the pokemon
        """
        return self._special_defense

    def set_special_defense(self, special_defense):
        """
        Set special defense of the pokemon
        """
        self._special_defense = special_defense

    def get_types(self):
        """
        Returns types of the pokemon
        """
        return self._types

    def get_burn(self):
        """
        Returns True if pokemon is burning else False
        """
        return self._burn

    def set_burn(self, burn:bool):
        """
        Set burn to True or False
        """
        self._burn = burn

    def get_legendary(self):
        """
        Returns True if pokemon is legendary else False
        """
        return self._legendary

    def get_speed(self):
        """
        Returns speed of the pokemon
        """
        return self._speed

    def __str__(self):
        """
        Returns string reprezentation of object
        """
        return (f"name: {self._name}, health: {self._health}, types: {self._types},\n"
        f"attack: {self._attack}, defense: {self._defense}, "
        f"special attack: {self._special_attack}, special defense: {self._special_defense}, "
        f"speed: {self._speed}, legendary: {self._legendary}, burn: {self._burn}")

    def actual_damage(self, weather, enemy_pokemon, type_attack):
        """
        Calculate damage made by attacker according to Bulbapedia formula
        """
        attack = self._attack if type_attack == "normal" else self._special_attack
        defense = enemy_pokemon.get_defense() if type_attack == "normal" else enemy_pokemon.get_special_defense()
        return round(((attack / defense * 1.5) + 2) \
             * self.attack_with_weather(weather) * self.critical_damage() * (randint(217, 255) / 255) \
             * self.attack_with_same_type(enemy_pokemon) * self.type_ratio(enemy_pokemon) * self.attack_when_burned(),2)


    def critical_damage(self):
        """
        Returns critical damage
        """
        list_of_damage = [1, 1, 1, 1, 1, 1, 1, 1, 1.5, 2]
        return choice(list_of_damage)

    def attack_with_weather(self, weather):
        """
        Returns attack rate depending on the weather and types of the pokemon
        """
        if (weather == "rain" and "Water" in self.get_types()) or (weather == "harsch sunlight" and "Fire" in self.get_types()):
            return 1.5
        elif (weather == "rain" and "Fire" in self.get_types()) or (weather == "harsch sunlight" and "Water" in self.get_types()):
            return 0.5
        else:
            return 1

    def attack_with_same_type(self, pokemon):
        """
        Returns attack rate depending on whether two pokemons have common type
        """
        for type in pokemon.get_types():
            if type in self.get_types():
                return 1.5
        return 1

    def attack_when_burned(self):
        """
        Returns attack rate depending on whether it burns
        """
        if self.get_burn() is True:
            return 0.7
        else:
            return 1

    def type_ratio(self, pokemon):
        """
        Returns attack rate depending on types of the attacking and defending pokemon
        """
        list_of_ratio = []
        for type in self.get_types():
            if type != "":
                index = types_ratio_file.type_indices[type]
                for type_enemy in pokemon.get_types():
                    if type_enemy != "":
                        index_enemy = types_ratio_file.type_indices[type_enemy]
                        list_of_ratio.append(types_ratio_file.type_effectivenss[index][index_enemy])
        return max(list_of_ratio)


