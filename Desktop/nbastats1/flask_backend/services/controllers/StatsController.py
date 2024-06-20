from services.models import Game, Player_Game, Player, PlayerCTR, PlayerSTR, Team_Game, TeamHistorical, Team
from services.controllers.UpdateController import UpdateController
import json

class StatsController:

    def average(list):
        return sum(list) / len(list) if list else 0
    

    def average_minutes(minutes_list):
        if not minutes_list:
            return 0
        total_seconds = 0
        for minute in minutes_list:
            splitted = minute.split(":")
            total_seconds += ((int(splitted[0]) * 60) + int(splitted[1])) if len(splitted) == 2 else 0

        average_seconds = round(total_seconds / len(minutes_list))

        new_minutes = int(average_seconds // 60)
        new_seconds = average_seconds % 60

        return f'{new_minutes}:{new_seconds:02}'

    @staticmethod
    def get_current_season_team_stats(team_id):
        # print("In Stats controller:", team_id)
        team_name = (Team.query.filter_by(team_id=team_id).first()).full_name
        # Gets all of the player stats for the current season that have the matching Team_id
        team_stats = Player_Game.query.filter_by(team_id=team_id).all()

        # Creates a set of all of the player_ids that are on the team and have played in a game this season
        player_ids = list(set([player.player_id for player in team_stats]))

        # average_player_stats = {}

        labels = []
        min = []
        fgm = []
        fga = []
        fgpct = []
        fg3m = []
        fg3a = []
        fg3pct = []
        ftm = []
        fta = []
        ftpct = []
        oreb = []
        dreb = []
        reb = []
        ast = []
        stl = []
        blk = []
        tov = []
        pf = []
        pts = []

        for player_id in player_ids:
            player_stats = Player_Game.query.filter_by(player_id=player_id).all()


            try:
                player_name = (Player.query.filter_by(player_id=player_id).first()).full_name

            except:
                player_name = UpdateController.update_player_table(player_id)
                



            labels.append(player_name)
            min.append(StatsController.average_minutes([stat.minutes for stat in player_stats if stat.minutes]))
            fgm.append(round(StatsController.average([stat.fgm for stat in player_stats if stat.minutes]),2))
            fga.append(round(StatsController.average([stat.fga for stat in player_stats if stat.minutes]),2))
            fgpct.append(round(StatsController.average([stat.fg_pct for stat in player_stats if stat.minutes]) * 100,2))
            fg3m.append(round(StatsController.average([stat.fg3m for stat in player_stats if stat.minutes]),2))
            fg3a.append(round(StatsController.average([stat.fg3a for stat in player_stats if stat.minutes]),2))
            fg3pct.append(round(StatsController.average([stat.fg3_pct for stat in player_stats if stat.minutes]) * 100,2))
            ftm.append(round(StatsController.average([stat.ftm for stat in player_stats if stat.minutes]),2))
            fta.append(round(StatsController.average([stat.fta for stat in player_stats if stat.minutes]),2))
            ftpct.append(round(StatsController.average([stat.ft_pct for stat in player_stats if stat.minutes]) * 100,2))
            oreb.append(round(StatsController.average([stat.oreb for stat in player_stats if stat.minutes]),2))
            dreb.append(round(StatsController.average([stat.dreb for stat in player_stats if stat.minutes]),2))
            reb.append(round(StatsController.average([stat.reb for stat in player_stats if stat.minutes]),2))
            ast.append(round(StatsController.average([stat.ast for stat in player_stats if stat.minutes]),2))
            stl.append(round(StatsController.average([stat.stl for stat in player_stats if stat.minutes]),2))
            blk.append(round(StatsController.average([stat.blk for stat in player_stats if stat.minutes]),2))
            tov.append(round(StatsController.average([stat.tov for stat in player_stats if stat.minutes]),2))
            pf.append(round(StatsController.average([stat.pf for stat in player_stats if stat.minutes]),2))
            pts.append(round(StatsController.average([stat.pts for stat in player_stats if stat.minutes]),2))

            # player_dict = {"Minutes": StatsController.average_minutes([stat.minutes for stat in player_stats]),
            #             "Field Goals Made": round(StatsController.average([stat.fgm for stat in player_stats]),2),
            #             "Field Goals Attempted": round(StatsController.average([stat.fga for stat in player_stats]),2),
            #             "Field Goal Percentage": round(StatsController.average([stat.fg_pct for stat in player_stats]),2),
            #             "Three Pointers Made": round(StatsController.average([stat.fg3m for stat in player_stats]),2),
            #             "Three Pointers Attempted": round(StatsController.average([stat.fg3a for stat in player_stats]),2),
            #             "Three Pointer Percentage": round(StatsController.average([stat.fg3_pct for stat in player_stats]),2),
            #             "Free Throws Made": round(StatsController.average([stat.ftm for stat in player_stats]),2),
            #             "Free Throw Attempts": round(StatsController.average([stat.fta for stat in player_stats]),2),
            #             "Free Throw Percentage": round(StatsController.average([stat.ft_pct for stat in player_stats]),2),
            #             "Offensive Rebounds": round(StatsController.average([stat.oreb for stat in player_stats]),2),
            #             "Defensive Rebounds": round(StatsController.average([stat.dreb for stat in player_stats]),2),
            #             "Total Rebounds": round(StatsController.average([stat.reb for stat in player_stats]),2),
            #             "Assists": round(StatsController.average([stat.ast for stat in player_stats]),2),
            #             "Steals": round(StatsController.average([stat.stl for stat in player_stats]),2),
            #             "Blocks": round(StatsController.average([stat.blk for stat in player_stats]),2),
            #             "Turn Overs": round(StatsController.average([stat.tov for stat in player_stats]),2),
            #             "Personal Fouls": round(StatsController.average([stat.pf for stat in player_stats]),2),
            #             "Points": round(StatsController.average([stat.pts for stat in player_stats]),2)}
            
        #     average_player_stats[f'{player_name}'] = player_dict
        
        # Labels = [player for player in average_player_stats]
        # Points = [player["Points"] for player in average_player_stats]
        # Assists = [player["Assists"] for player in average_player_stats]
        # Rebounds = [player["Total Rebounds"] for player in average_player_stats]
        # Steals = [player["Steals"] for player in average_player_stats]
        # Blocks = [player["Blocks"] for player in average_player_stats]

        elem = {"team_name": team_name,
                "Names": labels,
                "Minutes": min,
                "Field_Goals_Made" : fgm,
                "Field_Goals_Attempted" : fga,
                "Field_Goal_Percentage" : fgpct,
                "Three_Pointers_Made" : fg3m,
                "Three_Pointers_Attempted" : fg3a,
                "Three_Pointer_Percentage" : fg3pct,
                "Free_Throws_Made" : ftm,
                "Free_Throw_Attempts" : fta,
                "Free_Throw_Percentage" : ftpct,
                "Offensive_Rebounds" : oreb,
                "Defensive_Rebounds" : dreb,
                "Total_Rebounds" : reb,
                "Assists" : ast,
                "Steals" : stl,
                "Blocks" : blk,
                "Turn_Overs" : tov,
                "Personal_Fouls" : pf,
                "Points" : pts}
        
        # print(elem)
        return elem


        # return {team_name: average_player_stats}
        # print({team_name: average_player_stats})
        

    @staticmethod
    def get_current_season_player_stats(player_id):
        player_info = Player.query.filter_by(player_id=player_id).first()
        player_stats = Player_Game.query.filter_by(player_id=player_id).all()

        name = player_info.full_name
        team_id = (Team.query.filter_by(team_id=str(player_stats[0].team_id)).first()).team_id
        game_ids = [entry.game_id for entry in player_stats]
        minutes = [entry.minutes for entry in player_stats]
        fgm = [entry.fgm for entry in player_stats]
        fga = [entry.fga for entry in player_stats]
        fg_pct = [entry.fg_pct for entry in player_stats]
        fg3m = [entry.fg3m for entry in player_stats]
        fg3a = [entry.fg3a for entry in player_stats]
        fg3_pct = [entry.fg3_pct for entry in player_stats]
        ftm = [entry.ftm for entry in player_stats]
        fta = [entry.fta for entry in player_stats]
        ft_pct = [entry.ft_pct for entry in player_stats]
        oreb = [entry.oreb for entry in player_stats]
        dreb = [entry.dreb for entry in player_stats]
        reb = [entry.reb for entry in player_stats]
        ast = [entry.ast for entry in player_stats]
        stl = [entry.stl for entry in player_stats]
        blk = [entry.blk for entry in player_stats]
        tov = [entry.tov for entry in player_stats]
        pf = [entry.pf for entry in player_stats]
        pts = [entry.pts for entry in player_stats]

        stats = {"Name": name,
                 "Team_Id": team_id,
                 "Stats":
                 {
                    "game_ids": game_ids,
                    "minutes": minutes,
                    "fgm": fgm,
                    "fga": fga,
                    "fg_pct": fg_pct,
                    "fg3m": fg3m,
                    "fg3a": fg3a,
                    "fg3_pct": fg3_pct,
                    "ftm": ftm,
                    "fta": fta,
                    "ft_pct": ft_pct,
                    "oreb": oreb,
                    "dreb": dreb,
                    "reb": reb,
                    "ast": ast,
                    "stl": stl,
                    "blk": blk,
                    "tov": tov,
                    "pf": pf,
                    "pts": pts
                 }}

        return stats
        

    @staticmethod
    def get_team_names():
        return [{'Name': team.full_name, 'Team_id': team.team_id} for team in Team.query.all()]

    @staticmethod
    def get_player_names():
        return [{'Name': player.full_name, 'Player_id': player.player_id} for player in Player.query.all() if player.is_active == True]