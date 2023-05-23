"""Import abstract class Game from file PythonLabs.models.game."""
from PythonLabs.models.game import Game


class MobileGame(Game):
    """Content of class MobileGame."""
    def __init__(self, publisher, tittle, year, genre, min_players, max_players):
        """
        Initializing a MobileGame instance.

        Args:
            publisher (str): publisher of the MobileGame.
            tittle (str): the title of the MobileGame.
            year (int): the year of the MobileGame.
            genre (str): the genre of the MobileGame.
            min_players (int): the minimal players in the MobileGame.
            max_players (int): the maximal players in the MobileGame.
        """
        super().__init__(publisher, tittle, year, min_players, max_players)
        self.genre = genre

    def connect_player(self):
        """Player connection method."""

    def disconnect_player(self):
        """Player disconnection method."""

    def __str__(self):
        return f"MobileGame(publisher={self.publisher}, tittle={self.tittle}, year={self.year}, " \
               f"genre={self.genre}, min_players={self.min_players}, " \
               f"max_players={self.max_players})"
