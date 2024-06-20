from flask import Blueprint, jsonify, request
from services.controllers import GameController, StatsController
# from services.config import db
# from services.models import *
# from nba_api.stats.endpoints import scoreboardv2
# from datetime import datetime, timedelta


nba_stats_api = Blueprint('nba_stats', __name__)

@nba_stats_api.route('/get_games', methods=['GET'])
def get_games():

    # must call tomorrow_games first as this will clear the table if it is a new day and there are no tomorrow_games in the database
    tomorrow_games = GameController.get_tomorrow_games()
    # tomorrow_games = []
    today_games = GameController.get_today_games()

    games_data = {'tomorrow_games' : tomorrow_games,
                  'today_games': today_games}
    
        
    return jsonify(games_data), 200



@nba_stats_api.route('/update_live_games', methods=['POST'])
def update_live_games():
    try:
        GameController._update_live_games()
        return jsonify({"message": "Live games updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    


@nba_stats_api.route('/get_team_summary/<int:team_id>', methods=['GET'])
def get_team_summary(team_id):

    print("Team ID:", team_id)
    info = StatsController.get_current_season_team_stats(str(team_id))
    try:
        return jsonify(info), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    


@nba_stats_api.route('/get_player_summary', methods=['GET'])
def get_player_summary():

    player_ids_str = request.args.get('player_ids', '').split(",")
    print("Player ID:", player_ids_str)

    player_info = []
    for player in player_ids_str:
        player_info.append(StatsController.get_current_season_player_stats(str(player)))

    try:
        return jsonify(player_info), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@nba_stats_api.route('/get_player_names', methods=['GET'])
def get_player_names():

    return StatsController.get_player_names()

@nba_stats_api.route('/get_team_names', methods=['GET'])
def get_team_info():
    
    return StatsController.get_team_names()