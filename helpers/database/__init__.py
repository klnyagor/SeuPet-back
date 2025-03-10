from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine

db = SQLAlchemy()

# Configurar o primeiro banco
# engine = create_engine(
#     'postgresql://postgres:PSWORD@localhost:PORT/NOME_DB'
# )

# db.engine = engine
# db.session.configure(bind=engine)