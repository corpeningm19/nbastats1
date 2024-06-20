# need to import all models here so the migration can build the tables as need
# follows the pattern

from .team import Team
from .player import Player
from .live_games import LiveGame
from .team_historical_stats import TeamHistorical
from .playerSeasonTotalRegular import PlayerSTR
from .playerCareerTotalRegular import PlayerCTR
from .game import Game
from .team_game import Team_Game
from .player_game import Player_Game
