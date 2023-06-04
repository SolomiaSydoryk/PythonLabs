"""Import abstract class Game from file PythonLabs.models.game."""
from PythonLabs.exeptions.max_players import TooManyPlayersException, logged
from PythonLabs.models.game import Game


class BoardGame(Game):
    """Content of class BoardGame."""
    def __init__(self, publisher, title, year, min_players, max_players, current_players=10):
        """
        Initializing a BoardGame instance.

        Args:
            publisher (str): publisher of the BoardGame.
            title (str): the title of the BoardGame.
            year (int): the year of the BoardGame.
            min_players (int): the minimal players in the BoardGame.
            max_players (int): the maximal players in the BoardGame.
            current_players (int): the current players in BoardGame.
        """
        features_set = {"board", "cards"}
        super().__init__(publisher, title, year, min_players, max_players, features_set)
        self.current_players = current_players

    @logged(TooManyPlayersException, 'file')
    def connect_player(self):
        """Player connection method."""
        if self.current_players < self.max_players:
            return self.current_players + 1
        else:
            raise TooManyPlayersException("Maximum number of players already reached.")

    def disconnect_player(self):
        """Player disconnection method."""
        if self.current_players > self.min_players:
            return self.current_players - 1
        else:
            return 0

    def __str__(self):
        return f"BoardGame(publisher={self.publisher}, tittle={self.title}, year={self.year}, " \
               f"min_players={self.min_players}, max_players={self.max_players}, " \
               f"current_players={self.current_players}, features={self.features_set})"
