from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine

db = SQLAlchemy()

# Configurar o primeiro banco
# engine = create_engine(
#     'postgresql://postgres:123456@localhost:5434/db_seupet'
# )

# db.engine = engine
# db.session.configure(bind=engine)