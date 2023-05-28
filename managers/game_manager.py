"""Import abstract class Game from file PythonLabs.models.game."""
from PythonLabs.models.game import Game


class GameManager:
    """Content of class GameManager."""

    def __init__(self):
        """Create a non-static field."""
        self._games = []

    def add_game(self, game: Game):
        """This method add game in list games."""
        self._games.append(game)

    def __len__(self):
        return len(self._games)

    def __getitem__(self, index):
        return self._games[index]

    def __iter__(self):
        return iter(self._games)

    def find_all_games_with_certain_publisher(self, name):
        """This method find all games with certain publisher."""
        print(f"\nAll games with {name} publisher")
        selected_games = [game for game in self._games if game.publisher == name]
        for game in selected_games:
            print(game)

    def find_all_games_with_year_more_than(self, value):
        """This method find all games in which year is more than specified."""
        print(f"\nAll games with year more than {value}")
        selected_games = [game for game in self._games if game.year > value]
        for game in selected_games:
            print(game)

    def print_dict_filter(self, _type):
        """Print filtered dictionary."""
        for game in self.games:
            print(f"\n{type(game).__name__} {game.title}")
            print(game.__dict_filter__(_type))

    @property
    def games(self):
        """Getter for variable games."""
        return self._games

    @games.setter
    def games(self, value):
        """Setter for variable games."""
        self._games = value
