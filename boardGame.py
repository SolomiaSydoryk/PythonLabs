class BoardGame:
    instance = 0

    def __init__(self, tittle="Any", min_players=2, max_players=4, current_players=3):
        self.tittle = tittle
        self.min_players = min_players
        self.max_players = max_players
        self.current_players = current_players

    def get_tittle(self):
        return self.tittle

    def get_min_players(self):
        return self.min_players

    def get_max_players(self):
        return self.max_players

    def get_current_players(self):
        return self.current_players

    def set_tittle(self, t):
        self.tittle = t

    def set_min_players(self, mn):
        self.min_players = mn

    def set_max_players(self, mx):
        self.max_players = mx

    def set_current_players(self, c):
        self.current_players = c

    def add_player(self):
        if self.current_players < self.max_players:
            return self.current_players + 1
        else:
            return 0

    def remove_player(self):
        if self.current_players > self.min_players:
            return self.current_players - 1
        else:
            return 0

    def can_play(self):
        if self.min_players <= self.current_players <= self.max_players:
            return True
        else:
            return False

    @staticmethod
    def get_instance():
        if not BoardGame.instance:
            BoardGame.instance = BoardGame()
        return BoardGame.instance

    def __str__(self):
        return "BoardGame(tittle={}, min_players={}, max_players={}, current_players={})"\
            .format(self.tittle, self.min_players, self.max_players, self.current_players)


games = [BoardGame(), BoardGame("Monopoly", 2, 8), BoardGame.get_instance(), BoardGame.get_instance()]

for game in games:
    print(game)
