from services.config import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, nullable=False)
    full_name = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'<Player {self.id} - Player_ID: {self.player_id} - Full_Name: {self.full_name} - First_Name: {self.first_name} - Last_Name: {self.last_name} - Is_Active: {self.is_active}>'
    