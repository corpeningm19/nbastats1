from services.config import db

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.String, nullable=False)
    full_name = db.Column(db.String, nullable=False)
    abbreviation = db.Column(db.String, nullable=False)
    nickname = db.Column(db.String, nullable=True)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    year_founded = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Team {self.id} - Team_Id: {self.team_id} - Full_Name: {self.full_name} - Abbreviation: {self.abbreviation} - Nickname: {self.nickname} - City: {self.city} - State: {self.state} - Year_Founded: {self.year_founded}>'