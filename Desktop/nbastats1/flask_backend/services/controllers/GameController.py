from datetime import datetime, timedelta
from services.models import LiveGame, Team
from nba_api.stats.endpoints import scoreboardv2
from nba_api.live.nba.endpoints import ScoreBoard
from services.config import db

class GameController:
    @classmethod
    def tomorrow(cls):
        return (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
    
    @classmethod
    def today(cls):
        return datetime.now().strftime('%Y-%m-%d')

    @staticmethod
    def get_today_games():
        games_in_DB = LiveGame.query.filter_by(date=GameController.today()).all()
        games = []
        # If no games were found in the LiveGame table that have today's date
        if not games_in_DB:
            games_resultSets = scoreboardv2.ScoreboardV2(game_date=GameController.today()).get_dict()['resultSets']

            print("Get Today Games Called")
            # Creates a list of today's games from the NBA API
            for game in games_resultSets[0]['rowSet']:
                info = {
                    'game_id': game[2],
                    'game_status_text': game[4],
                    'date': game[0].split('T')[0], 
                    'home_team_id': game[6],
                    'home_team_record': "",
                    'away_team_id': game[7],
                    'away_team_record': "",
                    'home_team_score': None,
                    'away_team_score': None,
                    'period': None
                    }
                games.append(info)

            for team in games_resultSets[1]['rowSet']:
                for game in games:
                    if team[3] == game['home_team_id']:
                        game['home_team_record'] = team[7]
                        break
                    elif team[3] == game['away_team_id']:
                        game['away_team_record'] = team[7]
                        break
                    else:
                        continue
            
            # print(games)

            # Adds the list of todays's games to the database, for future calls.
            for game in games:
                new_game = LiveGame(
                    game_id = game['game_id'],
                    game_status_text = game['game_status_text'],
                    date = game['date'],
                    home_team_id = game['home_team_id'],
                    home_team_record = game['home_team_record'],
                    away_team_id = game['away_team_id'],
                    away_team_record = game['away_team_record'],
                    home_team_score = game['home_team_score'],
                    away_team_score = game['away_team_score'],
                    period = game['period']
                )
                db.session.add(new_game)
            db.session.commit()

        # Else, games with today's date were found in database, returns those.         
        else:
            games = [{  'game_id': game.game_id,
                        'game_status_text': game.game_status_text,
                        'date': game.date,
                        'home_team_id': game.home_team_id,
                        'home_team_record': game.home_team_record,
                        'away_team_id': game.away_team_id,
                        'away_team_record': game.away_team_record,
                        'home_team_score' :game.home_team_score,
                        'away_team_score': game.away_team_score,
                        'period': game.period} for game in games_in_DB]
                
        games_data = []

        team_ids = {game['home_team_id'] for game in games}.union({game['away_team_id'] for game in games})
        team_ids_str = {str(id) for id in team_ids}
        teams = Team.query.filter(Team.team_id.in_(team_ids_str)).all()
        team_lookup = {team.team_id: team for team in teams}


        for game in games:
            home_team = team_lookup.get(str(game['home_team_id']))
            away_team = team_lookup.get(str(game['away_team_id']))

            game_info = {'game_id': game['game_id'],
                        'game_status_text': game['game_status_text'],
                        'date': game['date'],
                        'period': game['period'],
                        'home_team': {
                            'team_id': home_team.team_id,
                            'full_name': home_team.full_name,
                            'abbreviation': home_team.abbreviation,
                            'nickname': home_team.nickname,
                            'city': home_team.city,
                            'state': home_team.state,
                            'year_founded': home_team.year_founded,
                            'record': game['home_team_record'],
                            'home_team_score': game['home_team_score']},
                        'away_team': {
                            'team_id': away_team.team_id,
                            'full_name': away_team.full_name,
                            'abbreviation': away_team.abbreviation,
                            'nickname': away_team.nickname,
                            'city': away_team.city,
                            'state': away_team.state,
                            'year_founded': away_team.year_founded,
                            'record': game['away_team_record'],
                            'away_team_score': game['away_team_score']}
                        }

            games_data.append(game_info)

        return games_data


    @staticmethod
    def get_tomorrow_games():
        games_in_DB = LiveGame.query.filter_by(date=GameController.tomorrow()).all()
        games = []

        # If no games are found in live_games table that match tomorrow's date
        if not games_in_DB:
            # games = GameController._update_tomorrow_games()
            return []

        # Else, games with tomorrow's date were found in database, returns those.         
        else:
            games = [{  'game_id': game.game_id,
                        'game_status_text': game.game_status_text,
                        'date': game.date,
                        'home_team_id': game.home_team_id,
                        'home_team_record': game.home_team_record,
                        'away_team_id': game.away_team_id,
                        'away_team_record': game.away_team_record,
                        'home_team_score' :game.home_team_score,
                        'away_team_score': game.away_team_score,
                        'period': game.period} for game in games_in_DB]
        
        games_data = []

        team_ids = {game['home_team_id'] for game in games}.union({game['away_team_id'] for game in games})
        team_ids_str = {str(id) for id in team_ids}
        teams = Team.query.filter(Team.team_id.in_(team_ids_str)).all()
        team_lookup = {team.team_id: team for team in teams}


        for game in games:
            home_team = team_lookup.get(str(game['home_team_id']))
            away_team = team_lookup.get(str(game['away_team_id']))

            game_info = {'game_id': game['game_id'],
                        'game_status_text': game['game_status_text'],
                        'date': game['date'],
                        'period': game['period'],
                        'home_team': {
                            'team_id': home_team.team_id,
                            'full_name': home_team.full_name,
                            'abbreviation': home_team.abbreviation,
                            'nickname': home_team.nickname,
                            'city': home_team.city,
                            'state': home_team.state,
                            'year_founded': home_team.year_founded,
                            'record': game['home_team_record'],
                            'home_team_score': game['home_team_score']},
                        'away_team': {
                            'team_id': away_team.team_id,
                            'full_name': away_team.full_name,
                            'abbreviation': away_team.abbreviation,
                            'nickname': away_team.nickname,
                            'city': away_team.city,
                            'state': away_team.state,
                            'year_founded': away_team.year_founded,
                            'record': game['away_team_record'],
                            'away_team_score': game['away_team_score']}
                        }

            games_data.append(game_info)

        return games_data
    

    @staticmethod
    def _update_tomorrow_games():
        games = []

        # First delete all of the entries in the live_games table.
        try:
            LiveGame.query.delete()
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            raise Exception("Error deleting livegame database")

        # Query the NBA API to get the games' information for tomorrow.
        games_resultSets = scoreboardv2.ScoreboardV2(game_date=GameController.tomorrow()).get_dict()['resultSets']

        # Creates a list of tomorrow's games from the NBA API
        for game in games_resultSets[0]['rowSet']:
            info = {
                'game_id': game[2],
                'game_status_text': game[4],
                'date': game[0].split('T')[0], 
                'home_team_id': game[6],
                'home_team_record': "",
                'away_team_id': game[7],
                'away_team_record': "",
                'home_team_score': None,
                'away_team_score': None,
                'period': None
                }
            games.append(info)

        for team in games_resultSets[1]['rowSet']:
            for game in games:
                if team[3] == game['home_team_id']:
                    game['home_team_record'] = team[7]
                    break
                elif team[3] == game['away_team_id']:
                    game['away_team_record'] = team[7]
                    break
                else:
                    continue

        # Adds the list of tomorrow's games to the database, for future calls.
        for game in games:
            new_game = LiveGame(
                game_id = game['game_id'],
                game_status_text = game['game_status_text'],
                date = game['date'],
                home_team_id = game['home_team_id'],
                home_team_record = game['home_team_record'],
                away_team_id = game['away_team_id'],
                away_team_record = game['away_team_record'],
                home_team_score = game['home_team_score'],
                away_team_score = game['away_team_score'],
                period = game['period']
            )
            db.session.add(new_game)
        db.session.commit()

        return games  


    @staticmethod
    def _update_live_games():
        # all of the games in the database with today's date
        games_in_DB = LiveGame.query.filter_by(date=GameController.today()).all()
        live_games = ScoreBoard().get_dict()['scoreboard']
        # if there are games with today's date in the database, and the live game data is for today
        if games_in_DB and live_games['gameDate'] == GameController.today():
            
            for old_game in games_in_DB:
                for live_game in live_games['games']:
                    # If it's a matching game id and the gamestatustext has changed, update the live game.
                    if old_game.game_id == live_game['gameId'] and (old_game.game_status_text != live_game['gameStatusText'] or old_game.home_team_score != live_game['homeTeam']['score'] or old_game.away_team_score != live_game['awayTeam']['score']):
                        old_game.game_status_text = live_game['gameStatusText']
                        old_game.home_team_score = live_game['homeTeam']['score']
                        old_game.away_team_score = live_game['awayTeam']['score']
                        old_game.period = live_game['period']
                        break
            
            db.session.commit()

    