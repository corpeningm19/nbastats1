from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost/NBAStats'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'

