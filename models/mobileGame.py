from PythonLabs.models.game import Game


class MobileGame(Game):
    def __init__(self, publisher, tittle, year, genre, min_players, max_players):
        super().__init__(publisher, tittle, year, min_players, max_players)
        self.genre = genre

    def connect_player(self):
        pass

    def disconnect_player(self):
        pass

    def __str__(self):
        return f"MobileGame(publisher={self.publisher}, tittle={self.tittle}, year={self.year}, genre={self.genre}, " \
               f"min_players={self.min_players}, max_players={self.max_players})"
