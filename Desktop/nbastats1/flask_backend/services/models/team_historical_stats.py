from services.config import db

class TeamHistorical(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer)
    team_city = db.Column(db.String(255))
    team_name = db.Column(db.String(255))
    year = db.Column(db.String(7))  # Assuming all years will be in the format 'YYYY-YY'
    gp = db.Column(db.Integer)
    wins = db.Column(db.Integer)
    losses = db.Column(db.Integer)
    win_pct = db.Column(db.Float)
    conf_rank = db.Column(db.Integer)
    div_rank = db.Column(db.Integer)
    po_wins = db.Column(db.Integer)
    po_losses = db.Column(db.Integer)
    conf_count = db.Column(db.Integer, nullable=True)
    div_count = db.Column(db.Integer)
    nba_finals_appearance = db.Column(db.String(255))  # 'N/A' or potentially 'Yes'/'No'
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
    pf = db.Column(db.Integer)
    stl = db.Column(db.Integer)
    tov = db.Column(db.Integer)
    blk = db.Column(db.Integer)
    pts = db.Column(db.Integer)
    pts_rank = db.Column(db.Integer)

    def __repr__(self):
        return f"<TeamHistorical {self.team_id} - TEAM_CITY {self.team_city} - TEAM_NAME - {self.team_name} - YEAR {self.year} - WINS {self.wins} - LOSSES {self.losses} - WIN_PCT {self.win_pct}>"