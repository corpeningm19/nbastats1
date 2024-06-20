from services.config import db


class PlayerCTR(db.Model):

    __tablename__ = 'player_career_total_regular'
    
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, nullable=False)
    league_id = db.Column(db.String(2), nullable=False)
    team_id = db.Column(db.Integer, nullable=False)
    gp = db.Column(db.Integer, nullable=True)
    gs = db.Column(db.Integer, nullable=True)  # Assuming GS can be null
    min = db.Column(db.Float, nullable=True)  # Assuming MIN can be null, using PostgreSQL FLOAT
    fgm = db.Column(db.Integer, nullable=True)
    fga = db.Column(db.Integer, nullable=True)
    fg_pct = db.Column(db.Float, nullable=True)
    fg3m = db.Column(db.Integer, nullable=True)
    fg3a = db.Column(db.Integer, nullable=True)
    fg3_pct = db.Column(db.Float, nullable=True)
    ftm = db.Column(db.Integer, nullable=True)
    fta = db.Column(db.Integer, nullable=True)
    ft_pct = db.Column(db.Float, nullable=True)
    oreb = db.Column(db.Integer, nullable=True)
    dreb = db.Column(db.Integer, nullable=True)
    reb = db.Column(db.Integer, nullable=True)
    ast = db.Column(db.Integer, nullable=True)
    stl = db.Column(db.Integer, nullable=True)
    blk = db.Column(db.Integer, nullable=True)
    tov = db.Column(db.Integer, nullable=True)
    pf = db.Column(db.Integer, nullable=True)
    pts = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'<CareerTotalsRegularSeason {self.player_id}>'
