from PythonLabs.models.game import Game


class BoardGame(Game):
    def __init__(self, publisher, tittle, year, min_players, max_players, current_players=3):
        super().__init__(publisher, tittle, year, min_players, max_players)
        self.current_players = current_players

    def connect_player(self):
        if self.current_players < self.max_players:
            return self.current_players + 1
        else:
            return 0

    def disconnect_player(self):
        if self.current_players > self.min_players:
            return self.current_players - 1
        else:
            return 0

    def __str__(self):
        return f"BoardGame(publisher={self.publisher}, tittle={self.tittle}, year={self.year}, " \
               f"min_players={self.min_players}, max_players={self.max_players}, " \
               f"current_players={self.current_players})"
