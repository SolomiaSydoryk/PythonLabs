from abc import ABC, abstractmethod


class Game(ABC):
    def __init__(self, publisher, tittle, year, min_players, max_players):
        self.publisher = publisher
        self.tittle = tittle
        self.year = year
        self.min_players = min_players
        self.max_players = max_players

    @abstractmethod
    def connect_player(self):
        pass

    def disconnect_player(self):
        pass
