from flask import Flask


blg = Flask(__name__)
blg.config.from_object('config')

from app import views
