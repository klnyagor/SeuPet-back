from flask_restful import fields
from sqlalchemy import String, Integer, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from helpers.database import db
from typing import List
from models.DateField import DateField

vacina_fields = {
    'id': fields.Integer,
    'nome_vacina': fields.String,
    'fabricante': fields.String,
    "data_validade": DateField(attribute='data_validade'),
    "lote": fields.String
}

class Vacina(db.Model):
    __tablename__ = 'vacina'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    nome_vacina: Mapped[str] = mapped_column(String(100), nullable=False)
    fabricante: Mapped[str] = mapped_column(String(100), nullable=False)
    data_validade: Mapped[Date] = mapped_column(Date, nullable=False)
    lote: Mapped[str] = mapped_column(String(50), nullable=False)

    # Relacionamento com Vacina_Animal
    registros: Mapped[List["Vacina_Animal"]] = relationship(back_populates="vacina", cascade="all, delete-orphan")

    def __init__(self, nome_vacina, fabricante, data_validade, lote):
        self.nome_vacina = nome_vacina
        self.fabricante = fabricante
        self.data_validade = data_validade
        self.lote = lote

    def __repr__(self) -> str:
        return f"<Vacina(nome_vacina={self.nome_vacina}, fabricante={self.fabricante}, data_validade={self.data_validade}, lote={self.lote})>"