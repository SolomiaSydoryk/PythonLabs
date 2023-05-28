"""Import abstract class Game from file PythonLabs.models.game."""
from PythonLabs.models.game import Game


class ComputerGame(Game):
    """Content of class ComputerGame."""
    def __init__(self, publisher, tittle, year, genre, min_players, max_players):
        """
        Initializing a ComputerGame instance.

        Args:
            publisher (str): publisher of the ComputerGame.
            tittle (str): the title of the ComputerGame.
            year (int): the year of the ComputerGame.
            genre (str): the genre of the ComputerGame.
            min_players (int): the minimal players in the ComputerGame.
            max_players (int): the maximal players in the ComputerGame.
        """
        super().__init__(publisher, tittle, year, min_players, max_players)
        self.genre = genre

    def connect_player(self):
        """Player connection method."""

    def disconnect_player(self):
        """Player disconnection method."""

    def __str__(self):
        return f"ComputerGame(publisher={self.publisher}, tittle={self.tittle}, year={self.year}, " \
               f"genre={self.genre}, min_players={self.min_players}, max_players={self.max_players})"
