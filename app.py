from helpers.application import app
from helpers.api import api
from helpers.cors import cors
from helpers.database import db

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:PSWORD@localhost:PORT/NOME_DB"

cors.init_app(app)
api.init_app(app)
db.init_app(app)

with app.app_context():
    db.create_all()