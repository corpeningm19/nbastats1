from services.config import db

class Player_Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, nullable=False)
    game_id = db.Column(db.String, nullable=False)
    team_id = db.Column(db.Integer, nullable=False)
    minutes = db.Column(db.String, nullable=False)  # Storing as INTERVAL for PostgreSQL. Adjust if using another DB.
    fgm = db.Column(db.Integer, nullable=False)
    fga = db.Column(db.Integer, nullable=False)
    fg_pct = db.Column(db.Float, nullable=False)
    fg3m = db.Column(db.Integer, nullable=False)
    fg3a = db.Column(db.Integer, nullable=False)
    fg3_pct = db.Column(db.Float, nullable=False)
    ftm = db.Column(db.Integer, nullable=False)
    fta = db.Column(db.Integer, nullable=False)
    ft_pct = db.Column(db.Float, nullable=False)
    oreb = db.Column(db.Integer, nullable=False)
    dreb = db.Column(db.Integer, nullable=False)
    reb = db.Column(db.Integer, nullable=False)
    ast = db.Column(db.Integer, nullable=False)
    stl = db.Column(db.Integer, nullable=False)
    blk = db.Column(db.Integer, nullable=False)
    tov = db.Column(db.Integer, nullable=False)
    pf = db.Column(db.Integer, nullable=False)
    pts = db.Column(db.Integer, nullable=False)
    plsmnspts = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Player_Game(id={self.id}, player_id={self.player_id}, game_id='{self.game_id}', team_id={self.team_id}, minutes='{self.minutes}', fieldGoalsMade={self.fgm}, fieldGoalsAttempted={self.fga}, fieldGoalsPercentage={self.fg_pct}, threePointersMade={self.fg3m}, threePointersAttempted={self.fg3a}, threePointersPercentage={self.fg3_pct}, freeThrowsMade={self.ftm}, freeThrowsAttempted={self.fta}, freeThrowsPercentage={self.ft_pct}, reboundsOffensive={self.oreb}, reboundsDefensive={self.dreb}, reboundsTotal={self.reb}, assists={self.ast}, steals={self.stl}, blocks={self.blk}, turnovers={self.tov}, foulsPersonal={self.pf}, points={self.pts}, plusMinusPoints={self.plsmnspts})>"