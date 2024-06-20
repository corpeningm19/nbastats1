from services.config import db

class Team_Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    season_id = db.Column(db.String)
    team_id = db.Column(db.Integer)
    team_abbreviation = db.Column(db.String)
    team_name = db.Column(db.String)
    game_id = db.Column(db.String)
    game_date = db.Column(db.Date)
    matchup = db.Column(db.String)
    wl = db.Column(db.String)
    minutes = db.Column(db.Integer)
    fgm = db.Column(db.Integer)
    fga = db.Column(db.Integer)
    fg_pct = db.Column(db.Float)
    fg3m = db.Column(db.Integer)
    fg3a = db.Column(db.Integer)
    fg3_pct = db.Column(db.Float)
    ftm = db.Column(db.Integer)
    fta = db.Column(db.Integer)
    ft_pct = db.Column(db.Float)
    oreb = db.Column(db.Integer)
    dreb = db.Column(db.Integer)
    reb = db.Column(db.Integer)
    ast = db.Column(db.Integer)
    stl = db.Column(db.Integer)
    blk = db.Column(db.Integer)
    tov = db.Column(db.Integer)
    pf = db.Column(db.Integer)
    pts = db.Column(db.Integer)
    plus_minus = db.Column(db.Integer)
    video_available = db.Column(db.Integer)

    def __repr__(self):
        return f"<Game(id={self.id}, game_id={self.game_id}, team_name={self.team_name}, game_date={self.game_date})>"
