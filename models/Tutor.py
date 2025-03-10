from flask_restful import fields
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from helpers.database import db
from typing import List

tutor_fields = {
    'id': fields.String,
    'nome': fields.String,
    'email': fields.String,
    'documentos': fields.String,
    'endereco_id': fields.String
}

class Tutor(db.Model):
    __tablename__ = 'tutor'
    id: Mapped[str] = mapped_column(String(20), primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False)
    documentos: Mapped[str] = mapped_column(String(100), nullable=False)

    endereco_id: Mapped[str] = mapped_column(ForeignKey("endereco.id"))
    endereco: Mapped["Endereco"] = relationship(back_populates='tutor', uselist=False)
    
    animais: Mapped[List["Animal"]] = relationship(back_populates='tutor')

    def __init__(self, nome, email, documentos, endereco_id):
        self.nome = nome
        self.email = email
        self.documentos = documentos
        self.endereco_id = endereco_id

    def __repr__(self) -> str:
        return f"Tutor(nome={self.nome}, email={self.email}, documentos={self.documentos}, endereco_id={self.endereco_id})"

