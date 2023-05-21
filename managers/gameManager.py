from PythonLabs.models.game import Game


class GameManager:
    __game_list = list()

    def add_game(self, game: Game):
        self.game_list.append(game)

    def find_all_games_with_certain_publisher(self, name):
        print(f"\nAll games with {name} publisher")
        selected_games = [game for game in self.game_list if game.publisher == name]
        for game in selected_games:
            print(game)

    def find_all_games_with_year_more_than(self, value):
        print(f"\nAll games with year more than {value}")
        selected_games = [game for game in self.__game_list if game.year > value]
        for game in selected_games:
            print(game)

    @property
    def game_list(self):
        return self.__game_list
