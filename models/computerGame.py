from PythonLabs.models.game import Game


class ComputerGame(Game):
    def __init__(self, publisher, tittle, year, genre, number_of_parts, min_players, max_players):
        super().__init__(publisher, tittle, year, min_players, max_players)
        self.genre = genre
        self.number_of_parts = number_of_parts

    def connect_player(self):
        pass

    def disconnect_player(self):
        pass

    def __str__(self):
        return f"ComputerGame(publisher={self.publisher}, tittle={self.tittle}, year={self.year}, " \
               f"genre={self.genre}, number_of_parts={self.number_of_parts}, min_players={self.min_players}, " \
               f"max_players={self.max_players})"
