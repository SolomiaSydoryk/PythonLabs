"""Import class BoardGame, ComputerGame, MobileGame, VideoGame from file models.
and class GameManager from file managers.gameManager."""
from models.board_game import BoardGame
from models.computer_game import ComputerGame
from models.mobile_game import MobileGame
from models.video_game import VideoGame
from managers.game_manager import GameManager

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
    result = list(game.connect_player() for game in games)
    print(result)

    result = [f"{game.title}: {index}" for index, game in enumerate(games)]
    print(result)

    game_connect_results = [game.connect_player() for game in games]
    result = [f"{game.title}: {connect_result}" for game, connect_result in zip(games, game_connect_results)]
    print(result)

    game_manager.print_filtered_dict(str)

    print(GameManager.all_games_satisfy_condition(games))
    print(GameManager.at_least_one_game_satisfies_condition(games))
