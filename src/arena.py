from random import choice


class Arena:
    """Class Arena. Contains attributes
    param player1: one of the players
    type player1: object

    param player2: second of the players
    type player2: object

    param weather: weather during the round
    type weather: str
    """
    def __init__(self, player1, player2, weather=None):
        self._weather= weather
        self._player1 = player1
        self._player2 = player2


    def get_weather(self):
        """
        Returns current weather.
        """
        return self._weather


    def get_player1(self):
        """
        Returns player1
        """
        return self._player1

    def get_player2(self):
        """
        Returns player2
        """
        return self._player2


    def pick_weather(self):
        """
        Randomly selects weather from available rain and harsch sunlight options.
        """
        self._weather = choice(["rain", "harsch sunlight", "clear skies"])

