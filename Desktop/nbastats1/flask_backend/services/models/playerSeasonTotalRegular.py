from services.config import db


class PlayerSTR(db.Model):
    __tablename__ = "player_season_total_regular"

    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, nullable=False)
    season_id = db.Column(db.String(7), nullable=False)
    league_id = db.Column(db.String(2), nullable=False)
    team_id = db.Column(db.BigInteger, nullable=False)
    team_abrv = db.Column(db.String(3), nullable=True)
    player_age = db.Column(db.Float, nullable=True)
    gp = db.Column(db.Integer, nullable=True)
    gs = db.Column(db.Integer, nullable=True) # Nullable because of zeros in your data, assuming it's intentional
    min = db.Column(db.Float, nullable=True)
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
        return f'<PlayerSTR: {self.id} - player_id: {self.player_id} - season_id: {self.season_id} - league_id: {self.league_id} - team_id: {self.team_id} - team_abrv: {self.team_abrv}'