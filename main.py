"""Import class BoardGame, ComputerGame, MobileGame, VideoGame from file PythonLabs.models.
and class GameManager from file PythonLabs.managers.gameManager."""
from PythonLabs.models.board_game import BoardGame
from PythonLabs.models.computer_game import ComputerGame
from PythonLabs.models.mobile_game import MobileGame
from PythonLabs.models.video_game import VideoGame
from PythonLabs.managers.game_manager import GameManager
from PythonLabs.managers.set_manager import SetManager

if __name__ == "__main__":
    game_manager = GameManager()
    game_manager.add_game(BoardGame("Parker Brothers", "Monopoly", 1935, 2, 8))
    game_manager.add_game(BoardGame("Hasbro", "Jenga", 1970, 2, 4))
    game_manager.add_game(ComputerGame("Rockstar Games", "GTA ", 2001, "Action-adventure", 1, 30))
    game_manager.add_game(ComputerGame("Focus Entertainment", "SnowRunner", 2021, "Simulator", 1, 4))
    game_manager.add_game(MobileGame("Krafton", "Pubg Mobile", 2018, "Battle Royal", 1, 4))
    game_manager.add_game(MobileGame("Supercell", "Clash of Clans", 2012, "Strategy", 1, 50))
    game_manager.add_game(VideoGame("GSC Game World", "S.T.A.L.K.E.R.", 2007, "Survival horror", 1, 1))
    game_manager.add_game(VideoGame("GSC Game World", "Cossacks", 2001, "Historical strategy", 1, 1))

    game_manager.find_all_games_with_certain_publisher("GSC Game World")
    game_manager.find_all_games_with_year_more_than(2005)

    games = game_manager.games
    result = [game.connect_player() for game in games]
    print(result)

    result = [f"{game.title}: {index}" for index, game in enumerate(games)]
    print(result)

    game_connect_results = [game.connect_player() for game in games]
    result = [f"{game.title}: {connect_result}" for game, connect_result in zip(games, game_connect_results)]
    print(result)

    game_manager.print_dict_filter(str)

    def all_games_satisfy_condition(games):
        """Searching for all games that match the condition"""
        all_satisfy = all(game.min_players >= 1 for game in games)
        return {"all": all_satisfy}

    def at_least_one_game_satisfies_condition(games):
        """Searching for at least one game that match the condition"""
        any_satisfy = any(game.max_players > 10 for game in games)
        return {"any": any_satisfy}

    print(all_games_satisfy_condition(games))
    print(at_least_one_game_satisfies_condition(games))

    sm = SetManager(game_manager)
    for feature in sm:
        print(feature)
