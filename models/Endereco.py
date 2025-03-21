from flask_restful import fields
from helpers.database import db
from sqlalchemy.orm import Mapped, mapped_column, relationship

endereco_fields = {
    'id': fields.Integer,
    'estado': fields.String,
    'cep': fields.String,
    'cidade': fields.String,
    'bairro': fields.String,
    'rua': fields.String,
    'numero': fields.Integer,
    'complemento': fields.String
}

class Endereco(db.Model):
    __tablename__ = 'endereco'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    estado: Mapped[str] = mapped_column()
    cep: Mapped[str] = mapped_column()
    cidade: Mapped[str] = mapped_column()
    bairro: Mapped[str] = mapped_column()
    rua: Mapped[str] = mapped_column()
    numero: Mapped[int] = mapped_column()
    complemento: Mapped[str] = mapped_column()

    tutor: Mapped["Tutor"] = relationship('Tutor', back_populates='endereco', uselist=False, cascade="all, delete-orphan", single_parent=True)

    def __init__(self, estado, cep, cidade, bairro, rua, numero, complemento):
        self.estado = estado
        self.cep = cep
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.numero = numero
        self.complemento = complemento