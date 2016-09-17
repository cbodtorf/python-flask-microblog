from flask import Flask
from flask_sqlalchemy import SQLAlchemy


blg = Flask(__name__)
blg.config.from_object('config')
db = SQLAlchemy(blg)

from app import views, models
