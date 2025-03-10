from flask_restful import fields
from sqlalchemy import ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from helpers.database import db
from typing import List

animal_fields = {
    'id': fields.String,
    'nome': fields.String,
    'data_nascimento': fields.Date,
    'especie': fields.String,
    'raca': fields.String,
    'peso': fields.Float,
    'porte': fields.String,
    'pelagem': fields.String,
    'cadastro': fields.String,
    'foto': fields.String,

    'tutor_id': fields.String
}

class Animal(db.Model):
    __tablename__ = 'animal'
    
    id: Mapped[str] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column()
    dataNascimento: Mapped[Date] = mapped_column(Date)
    especie: Mapped[str] = mapped_column()
    raca: Mapped[str] = mapped_column()
    peso: Mapped[float] = mapped_column()
    porte: Mapped[str] = mapped_column()
    pelagem: Mapped[str] = mapped_column()
    cadastro: Mapped[str] = mapped_column()
    foto: Mapped[str] = mapped_column()
    
    tutor_id: Mapped[str] = mapped_column(ForeignKey('tutor.id'))
    tutor: Mapped["Tutor"] = relationship(back_populates="animais")

    vermifugacoes: Mapped[List["Vermifugacao"]] = relationship(back_populates="animal")
    saudes: Mapped[List["Saude"]] = relationship(back_populates="animal")
    vacinas: Mapped[List["Vacina"]] = relationship(back_populates="animal")
    doencas: Mapped[List["Doenca"]] = relationship(back_populates="animal")

    def __init__(self, nome, dataNascimento, especie, raca, peso, porte, pelagem, cadastro, foto, tutor_id):
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.especie = especie
        self.raca = raca
        self.peso = peso
        self.porte = porte
        self.pelagem = pelagem
        self.cadastro = cadastro
        self.foto = foto

        self.tutor_id = tutor_id

    def __repr__(self) -> str:
        return f"Animal(nome={self.nome}, dataNascimento={self.dataNascimento}, especie={self.especie}, raca={self.raca}, peso={self.peso}, porte={self.porte}, pelagem={self.pelagem}, cadastro={self.cadastro}, tutor_id={self.tutor_id})"