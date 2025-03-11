from helpers.application import app
from helpers.cors import cors
from helpers.api import api
from helpers.database import db
from models.Tutor import Tutor

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:123456@localhost:5434/db_seupet"

cors.init_app(app)
api.init_app(app)
db.init_app(app)

with app.app_context():
    db.create_all()