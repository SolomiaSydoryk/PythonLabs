"""Import abstract class Game from file PythonLabs.models.game."""
from PythonLabs.models.game import Game


class GameManager:
    """Content of class GameManager."""
    def __init__(self):
        """Create a non-static field."""
        self.games = []

    def add_game(self, game: Game):
        """This method add game in list games."""
        self.games.append(game)

    def find_all_games_with_certain_publisher(self, name):
        """This method find all games with certain publisher."""
        print(f"\nAll games with {name} publisher")
        selected_games = [game for game in self.games if game.publisher == name]
        return selected_games

    def find_all_games_with_year_more_than(self, value):
        """This method find all games in which year is more than specified."""
        print(f"\nAll games with year more than {value}")
        selected_games = [game for game in self.games if game.year > value]
        return selected_games

    @property
    def games(self):
        """Getter for variable games."""
        return self.games

    @games.setter
    def games(self, value):
        """Setter for variable games."""
        self._games = value
