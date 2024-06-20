from services.config import db


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.String, primary_key=True)
    season = db.Column(db.String, nullable=False)
    date = db.Column(db.String,nullable=False)
    away_team_id = db.Column(db.Integer, nullable=False)
    home_team_id = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return f'<Game - Id: {self.id} - Game_id: {self.game_id} - Season: {self.season} - Date: {self.date} - Away_Team_Id: {self.away_team_id} - Away_Game_Index: {self.away_game_index} - Home_Team_Id: {self.home_team_id} - Home_Game_Index: {self.home_game_index}>'
