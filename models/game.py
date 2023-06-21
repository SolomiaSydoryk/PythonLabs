"""Import ABC, abstractmethod from abc."""
from abc import ABC, abstractmethod


class Game(ABC):
    """Content of abstract class Game."""
    def __init__(self, publisher, title, year, min_players, max_players, features_set):
        """
        Initializing a Game instance.

        Args:
            publisher (str): publisher of the Game.
            title (str): the title of the Game.
            year (int): the year of the Game.
            min_players (int): the minimal players in the Game.
            max_players (int): the maximal players in the Game.
            features_set (set): a set of features of the Game.
        """
        self.publisher = publisher
        self.title = title
        self.year = year
        self.min_players = min_players
        self.max_players = max_players
        self.features_set = features_set

    def __iter__(self):
        """Return an iterator over the features set."""
        return iter(self.features_set)

    @abstractmethod
    def connect_player(self):
        """Player connection abstract method."""

    @abstractmethod
    def disconnect_player(self):
        """Player disconnection abstract method."""

    def __dict_filter__(self, _type):
        """Filter __dict__ keys and values by their types."""
        result = {}
        for key, value in self.__dict__.items():
            if isinstance(value, _type):
                result[key] = value
        return result
