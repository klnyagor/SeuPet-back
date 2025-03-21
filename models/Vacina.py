# from flask_restful import fields
# from sqlalchemy import Date
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from helpers.database import db
# from typing import List, Optional

# from models.Vacina_Animal import Vacina_Animal

# vacina_fields = {
#     'id': fields.Integer,
#     'nome_vacina': fields.String,
#     'fabricante': fields.String,
#     "data_validade": Date,
#     "lote": fields.String
# }

# class Vacina(db.Model):
#     __tablename__ = 'vacina'
    
#     id: Mapped[str] = mapped_column(primary_key=True)
#     nome_vacina: Mapped[str] = mapped_column()
#     fabricante: Mapped[str] = mapped_column()
#     data_validade: Mapped[Date] = mapped_column(Date)
#     lote: Mapped[str] = mapped_column()

#     animais = Mapped[List["Vacina_Animal"]] = relationship(back_populates="vacina")

#     def __init__(self, nome_vacina, fabricante, data_vailidade, lote):
#         self.nome_vacina = nome_vacina
#         self.fabricante = fabricante
#         self.data_validade = data_vailidade
#         self.lote = lote

#     def __repr__(self) -> str:
#         return f"<Vacina(vacina={self.nome_vacina}, fabricante={self.fabricante}, data_validade={self.data_validade}, lote={self.lote})>"
