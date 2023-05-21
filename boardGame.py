class BoardGame:
    __instance = None

    def __init__(self, tittle="Any", min_players=2, max_players=4, current_players=3):
        """
        Initializing a BoardGame instance.

        Args:
            tittle (str): the title of the BoardGame.
            min_players (int): the minimal players in the BoardGame.
            max_players (int): the maximal players in the BoardGame.
            current_players (int): the current players in BoardGame.
        """
        self.tittle = tittle
        self.min_players = min_players
        self.max_players = max_players
        self.current_players = current_players

    def add_player(self):
        """Increasing the current_players to +1. Else - setting the current_players to 0."""
        if self.current_players < self.max_players:
            return self.current_players + 1
        else:
            return 0

    def remove_player(self):
        """Decreasing the current_players to -1. Else - setting the current_players to 0."""
        if self.current_players > self.min_players:
            return self.current_players - 1
        else:
            return 0

    def can_play(self):
        """Decreasing current_players to -1. Else - setting current_players to 0."""
        if self.min_players <= self.current_players <= self.max_players:
            return True
        else:
            return False

    @staticmethod
    def get_instance():
        """
        Getting an instance of the BoardGame class.
        Returns:
        BoardGame: The singleton instance of the BoardGame class.
        """
        if not BoardGame.__instance:
            BoardGame.__instance = BoardGame()
        return BoardGame.__instance

    def __str__(self):
        """Returning a string representation of BoardGame class."""
        return "BoardGame(tittle={}, min_players={}, max_players={}, current_players={})" \
            .format(self.tittle, self.min_players, self.max_players, self.current_players)


if __name__ == "__main__":
    games = [BoardGame(), BoardGame("Monopoly", 2, 8), BoardGame.get_instance(), BoardGame.get_instance()]
    for game in games:
        print(game)
