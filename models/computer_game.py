"""Import abstract class Game from file models.game."""
from models.game import Game


class ComputerGame(Game):
    """Content of class ComputerGame."""
    def __init__(self, publisher, title, year, genre, min_players, max_players):
        """
        Initializing a ComputerGame instance.

        Args:
            publisher (str): publisher of the ComputerGame.
            title (str): the title of the ComputerGame.
            year (int): the year of the ComputerGame.
            genre (str): the genre of the ComputerGame.
            min_players (int): the minimal players in the ComputerGame.
            max_players (int): the maximal players in the ComputerGame.
        """
        features_set = {"online multiplayer", "achievements"}
        super().__init__(publisher, title, year, min_players, max_players, features_set)
        self.genre = genre

    def connect_player(self):
        """Player connection method."""

    def disconnect_player(self):
        """Player disconnection method."""

    def __str__(self):
        return f"ComputerGame(publisher={self.publisher}, tittle={self.title}, year={self.year}, " \
               f"genre={self.genre}, min_players={self.min_players}, max_players={self.max_players}, " \
               f"features={self.features_set})"
