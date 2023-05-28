"""Import class BoardGame, ComputerGame, MobileGame, VideoGame from file PythonLabs.models.
and class GameManager from file PythonLabs.managers.gameManager."""
from PythonLabs.models.boardGame import BoardGame
from PythonLabs.models.computerGame import ComputerGame
from PythonLabs.models.mobileGame import MobileGame
from PythonLabs.models.videoGame import VideoGame
from PythonLabs.managers.gameManager import GameManager

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

    for game in game_manager.games:
        print(game)

    game_manager.find_all_games_with_certain_publisher("GSC Game World")
    game_manager.find_all_games_with_year_more_than(2005)
