"""Import abstract class Game from file PythonLabs.models.game."""
from PythonLabs.models.game import Game


class MobileGame(Game):
    """Content of class MobileGame."""
    def __init__(self, publisher, title, year, genre, min_players, max_players):
        """
        Initializing a MobileGame instance.

        Args:
            publisher (str): publisher of the MobileGame.
            title (str): the title of the MobileGame.
            year (int): the year of the MobileGame.
            genre (str): the genre of the MobileGame.
            min_players (int): the minimal players in the MobileGame.
            max_players (int): the maximal players in the MobileGame.
        """
        features_set = {"offline play", "in-app purchases"}
        super().__init__(publisher, title, year, min_players, max_players, features_set)
        self.genre = genre

    def connect_player(self):
        """Player connection method."""

    def disconnect_player(self):
        """Player disconnection method."""

    def __str__(self):
        return f"MobileGame(publisher={self.publisher}, tittle={self.title}, year={self.year}, " \
               f"genre={self.genre}, min_players={self.min_players}, " \
               f"max_players={self.max_players}, features={self.features_set})"
