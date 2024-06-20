from services.config import db

class LiveGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.String, nullable=False)
    game_status_text = db.Column(db.String, nullable=False)
    date = db.Column(db.String,nullable=False)
    home_team_id = db.Column(db.Integer, nullable=False)
    home_team_record = db.Column(db.String, nullable=False)
    away_team_id = db.Column(db.Integer, nullable=False)
    away_team_record = db.Column(db.String, nullable=False)
    home_team_score = db.Column(db.Integer, nullable=True)
    away_team_score = db.Column(db.Integer, nullable=True)
    period = db.Column(db.Integer, nullable=True)


    def __repr__(self):
       return f'< ID {self.id} - GameID: {self.game_id} - GameStatusText: {self.game_status_text} - Date: {self.date} - HomeTeamID: {self.home_team_id} - HomeTeamRecord: {self.home_team_record} - AwayTeamID: {self.away_team_id} - AwayTeamRecord: {self.away_team_record} - HomeTeamScore: {self.home_team_score} - AwayTeamScore: {self.away_team_score} - Period: {self.period}>'