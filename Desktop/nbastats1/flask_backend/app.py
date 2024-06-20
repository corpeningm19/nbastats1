from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from services.config import Config, db
from apscheduler.schedulers.background import BackgroundScheduler
from services.routes.api_routes import api_bp
from services.routes.nba_stats import nba_stats_api
from services.models import *
from services.controllers import *

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

# Initialize SQLAlchemy and Migrate
db.init_app(app)
migrate = Migrate(app, db)

def update_live_games_with_context():
    with app.app_context():
        GameController._update_live_games()

def update_tomorrow_games_with_context():
    with app.app_context():
        GameController._update_tomorrow_games()

with app.app_context():
    db.create_all()
    GameController._update_tomorrow_games()
    # Updates the player_game and team_game tables with the latest information, if back-end launch fails due to upload,
    # comment the line below to disable the updater.
    UpdateController.update_team_player_games()
    # StatsController.get_current_season_player_stats("1626172")
    scheduler = BackgroundScheduler(daemon=True)
    # Wrap the GameController._update_live_games call to ensure it's executed within an app context
    scheduler.add_job(update_live_games_with_context, 'interval', seconds=30)
    scheduler.add_job(update_tomorrow_games_with_context, 'interval', days=1)
    scheduler.start()

# Register blueprints
app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(nba_stats_api, url_prefix='/nba_stats')

if __name__ == '__main__':
    app.run(use_reloader=False)