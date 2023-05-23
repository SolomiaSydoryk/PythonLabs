"""Import abstract class Game from file PythonLabs.models.game."""
from PythonLabs.models.game import Game


class VideoGame(Game):
    """Content of class VideoGame."""
    def __init__(self, publisher, tittle, year, genre, min_players, max_players):
        """
        Initializing a VideoGame instance.

        Args:
            publisher (str): publisher of the VideoGame.
            tittle (str): the title of the VideoGame.
            year (int): the year of the VideoGame.
            genre (str): the genre of the VideoGame.
            min_players (int): the minimal players in the VideoGame.
            max_players (int): the maximal players in the VideoGame.
        """
        super().__init__(publisher, tittle, year, min_players, max_players)
        self.genre = genre

    def connect_player(self):
        """Player connection method."""

    def disconnect_player(self):
        """Player disconnection method."""

    def __str__(self):
        return f"VideoGame(publisher={self.publisher}, tittle={self.tittle}, year={self.year}, " \
               f"genre={self.genre}, min_players={self.min_players}, " \
               f"max_players={self.max_players})"
