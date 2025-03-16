from flask_restful import fields
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from helpers.database import db
from models.Endereco import endereco_fields
from typing import List, Optional

tutor_fields = {
    'id': fields.Integer,
    'nome': fields.String,
    'email': fields.String,
    'documento': fields.String,
    # 'endereco_id': fields.Integer
    'endereco': fields.Nested(endereco_fields)
}

class Tutor(db.Model):
    __tablename__ = 'tutor'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False)
    documento: Mapped[str] = mapped_column(String(20), nullable=False)

    endereco_id: Mapped[int] = mapped_column(ForeignKey("endereco.id"))
    endereco: Mapped["Endereco"] = relationship(back_populates='tutor', uselist=False)

    animais: Mapped[Optional[List["Animal"]]] = relationship(back_populates='tutor', cascade="all, delete-orphan")

    def __init__(self, nome, email, documento, endereco_id): 
        self.nome = nome
        self.email = email
        self.documento = documento
        self.endereco_id = endereco_id

    def __repr__(self) -> str:
        return f"<Tutor(nome={self.nome}, email={self.email}, documento={self.documento}, endereco_id={self.endereco_id})>"

