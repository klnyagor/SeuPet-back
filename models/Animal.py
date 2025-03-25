from flask_restful import fields
from sqlalchemy import ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from helpers.database import db
from typing import List
from models.DateField import DateField

from models.Tutor import tutor_fields

animal_fields = {
    'id': fields.Integer,
    'nome': fields.String,
    'dataNascimento': DateField(attribute='dataNascimento'),
    'especie': fields.String,
    'raca': fields.String,
    'peso': fields.Float,
    'porte': fields.String,
    'pelagem': fields.String,
    'cadastro': fields.String,
    # 'foto': fields.String,

    'tutor': fields.Nested(tutor_fields),
}

class Animal(db.Model):
    __tablename__ = 'animal'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column()
    dataNascimento: Mapped[Date] = mapped_column(Date)
    especie: Mapped[str] = mapped_column()
    raca: Mapped[str] = mapped_column()
    peso: Mapped[float] = mapped_column()
    porte: Mapped[str] = mapped_column()
    pelagem: Mapped[str] = mapped_column()
    cadastro: Mapped[str] = mapped_column()
    # foto: Mapped[str] = mapped_column()
    
    tutor_id: Mapped[int] = mapped_column(ForeignKey('tutor.id'))
    tutor: Mapped["Tutor"] = relationship(back_populates="animais")

    #Relacionamento com Vacina_Animal
    vacinas: Mapped[List["Vacina_Animal"]] = relationship(back_populates='animal', cascade='all, delete-orphan')

    def __init__(self, nome, dataNascimento, especie, raca, peso, porte, pelagem, cadastro, tutor_id): #, foto
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.especie = especie
        self.raca = raca
        self.peso = peso
        self.porte = porte
        self.pelagem = pelagem
        self.cadastro = cadastro
        # self.foto = foto

        self.tutor_id = tutor_id

    def __repr__(self) -> str:
        return f"Animal(nome={self.nome}, dataNascimento={self.dataNascimento}, especie={self.especie}, raca={self.raca}, peso={self.peso}, porte={self.porte}, pelagem={self.pelagem}, cadastro={self.cadastro}, tutor_id={self.tutor_id})"