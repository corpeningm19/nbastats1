from nba_api.stats.endpoints import leaguegamelog, boxscoretraditionalv3
# from nba_api.stats.static import players
from nba_api.stats.endpoints import commonallplayers
from sqlalchemy.exc import IntegrityError
import random, time
from services.models import *
from services.config import db
from flask import current_app


class UpdateController:
    
    # Returns a list of all of the game_ids that have been uploaded into the team__game table
    @classmethod
    def get_uploaded_games(cls):
        return [game_id[0] for game_id in Team_Game.query.with_entities(Team_Game.game_id).distinct().all()]

    @staticmethod
    def test():
        print("This is a test")

    @staticmethod
    def update_team_player_games():
        # All current season team_game stats from nba_api
        team_game_stats = leaguegamelog.LeagueGameLog(season='2023-24',).get_dict()['resultSets'][0]['rowSet']

        # Gets the quantity of games that have not been uploaded to the database.
        # remaining = len([game_id for game_id in team_game_stats if game_id[4] not in already_uploaded])

        for team in team_game_stats:
            existing_record = Team_Game.query.filter_by(game_id=team[4], team_id=team[1]).first()
            
            # If a record already exists for that team in that game
            if existing_record:
                # If the current record is from a game that was ongoing when it last checked, and there
                # is a WL record now, update the record 
                if existing_record.wl is None and team[7] is not None:
                    print(f"Updating game_id {team[4]} for team {team[1]}")
                    existing_record.wl = team[7]
                    existing_record.minutes = team[8]
                    existing_record.fgm = team[9]
                    existing_record.fga = team[10]
                    existing_record.fg_pct = team[11]
                    existing_record.fg3m = team[12]
                    existing_record.fg3a = team[13]
                    existing_record.fg3_pct = team[14]
                    existing_record.ftm = team[15]
                    existing_record.fta = team[16]
                    existing_record.ft_pct = team[17]
                    existing_record.oreb = team[18]
                    existing_record.dreb = team[19]
                    existing_record.reb = team[20]
                    existing_record.ast = team[21]
                    existing_record.stl = team[22]
                    existing_record.blk=  team[23]
                    existing_record.tov = team[24]
                    existing_record.pf = team[25]
                    existing_record.pts = team[26]
                    existing_record.plus_minus = team[27]
                    db.session.commit()

                    # Add the player stats to the player__game table
                    UpdateController.update_player_game(team[4])

            else:
                print(f'Uploading game: {team[4]}')
                
                new_record = Team_Game(
                    season_id = team[0],
                    team_id = team[1],
                    team_abbreviation = team[2],
                    team_name = team[3],
                    game_id = team[4],
                    game_date = team[5],
                    matchup = team[6],
                    wl = team[7],
                    minutes = team[8],
                    fgm = team[9],
                    fga = team[10],
                    fg_pct = team[11],
                    fg3m = team[12],
                    fg3a = team[13],
                    fg3_pct = team[14],
                    ftm = team[15],
                    fta = team[16],
                    ft_pct = team[17],
                    oreb = team[18],
                    dreb = team[19],
                    reb = team[20],
                    ast = team[21],
                    stl = team[22],
                    blk=  team[23],
                    tov = team[24],
                    pf = team[25],
                    pts = team[26],
                    plus_minus = team[27],
                    video_available = team[28])
                
                db.session.add(new_record)
                try:
                    db.session.commit()
                    # Calls player_game update method to update individual player stats for each game if the game has finished
                    # and there is a WL record for each team on the game.
                    if team[7] is not None:
                        UpdateController.update_player_game(team[4])

                except IntegrityError:
                    db.session.rollback()
                    # Handle the conflict (e.g., ignore, log it, or update existing record)
                    print("Record with this ID already exists, ignoring insert.")
                


    @staticmethod
    def update_player_game(game_id):
        wait_time = random.randint(2,5)

        # Grabs the player statistics for the supplied game_id from the nba_api
        data = boxscoretraditionalv3.BoxScoreTraditionalV3(game_id).get_dict()['boxScoreTraditional']

        home_team = data['homeTeam']
        away_team = data['awayTeam']

        for player in home_team['players']:
            stats = player['statistics']

            existing_player_game = Player_Game.query.filter_by(game_id=game_id, player_id=player['personId']).first()

            if not existing_player_game:
                new_record = Player_Game(
                    player_id = player['personId'],
                    game_id = game_id,
                    team_id = home_team['teamId'],
                    minutes = stats['minutes'],
                    fgm = stats['fieldGoalsMade'],
                    fga = stats['fieldGoalsAttempted'],
                    fg_pct = stats['fieldGoalsPercentage'],
                    fg3m = stats['threePointersMade'],
                    fg3a = stats['threePointersAttempted'],
                    fg3_pct = stats['threePointersPercentage'],
                    ftm = stats['freeThrowsMade'],
                    fta = stats['freeThrowsAttempted'],
                    ft_pct = stats['freeThrowsPercentage'],
                    oreb = stats['reboundsOffensive'],
                    dreb = stats['reboundsDefensive'],
                    reb = stats['reboundsTotal'],
                    ast = stats['assists'],
                    stl = stats['steals'],
                    blk = stats['blocks'],
                    tov = stats['turnovers'],
                    pf = stats['foulsPersonal'],
                    pts = stats['points'],
                    plsmnspts = stats['plusMinusPoints'])
                
                db.session.add(new_record)
                
                try:
                    db.session.commit()
                except IntegrityError:
                    db.session.rollback()
                    # Handle the conflict - this might be logging or another form of notification
                    print("Record with this ID already exists, ignoring insert.")


        for player in away_team['players']:
            stats = player['statistics']


            existing_player_game = Player_Game.query.filter_by(game_id=game_id, player_id=player['personId']).first()
                
            if not existing_player_game:

                new_record = Player_Game(
                    player_id = player['personId'],
                    game_id = game_id,
                    team_id = away_team['teamId'],
                    minutes = stats['minutes'],
                    fgm = stats['fieldGoalsMade'],
                    fga = stats['fieldGoalsAttempted'],
                    fg_pct = stats['fieldGoalsPercentage'],
                    fg3m = stats['threePointersMade'],
                    fg3a = stats['threePointersAttempted'],
                    fg3_pct = stats['threePointersPercentage'],
                    ftm = stats['freeThrowsMade'],
                    fta = stats['freeThrowsAttempted'],
                    ft_pct = stats['freeThrowsPercentage'],
                    oreb = stats['reboundsOffensive'],
                    dreb = stats['reboundsDefensive'],
                    reb = stats['reboundsTotal'],
                    ast = stats['assists'],
                    stl = stats['steals'],
                    blk = stats['blocks'],
                    tov = stats['turnovers'],
                    pf = stats['foulsPersonal'],
                    pts = stats['points'],
                    plsmnspts = stats['plusMinusPoints'])
                
                db.session.add(new_record)
                
                try:
                    db.session.commit()
                except IntegrityError:
                    db.session.rollback()
                    print("Record with this ID already exists, ignoring insert.")
        
        print(f'Sleeping {wait_time} seconds between game entry')
        time.sleep(wait_time)


    @staticmethod
    def update_player_table(player_id):
        print("player_id:", player_id)


        with current_app.app_context():
            player_in = Player.query.filter_by(player_id=player_id).first()

            if not player_in:
                all_players = commonallplayers.CommonAllPlayers(1,"00","2023-24").get_dict()['resultSets'][0]['rowSet']
                for each in all_players:
                    if each[0] == player_id:
                        player_name = each[2].split(' ')
                        break

                # player_info = players.find_player_by_id(player_id)
                print("Missing Player Info:", player_name)
                new_player = Player(player_id=player_id,
                                    full_name=" ".join(player_name),
                                    first_name=player_name[0],
                                    last_name=player_name[1],
                                    is_active=True)
                
                db.session.add(new_player)
                db.session.commit()

                return " ".join(player_name)