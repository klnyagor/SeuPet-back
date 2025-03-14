from flask_restful import fields
from sqlalchemy.orm import Mapped, mapped_column, relationship
from helpers.database import db

endereco_fields = {
    'id': fields.String,
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

    id: Mapped[str] = mapped_column(primary_key=True, nullable=False)
    estado: Mapped[str] = mapped_column(nullable=False)
    cep: Mapped[str] = mapped_column(nullable=False)
    cidade: Mapped[str] = mapped_column(nullable=False)
    bairro: Mapped[str] = mapped_column(nullable=False)
    rua: Mapped[str] = mapped_column(nullable=False)
    numero: Mapped[int] = mapped_column()
    complemento: Mapped[str] = mapped_column()
    
    tutor: Mapped["Tutor"] = relationship("Tutor", back_populates='endereco', uselist=False)

    def __init__(self, estado, cep, cidade, bairro, rua, numero, complemento):
        self.estado = estado
        self.cep = cep
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.numero = numero
        self.complemento = complemento

    def __repr__(self) -> str:
        return f"Endereco(estado={self.estado}, cep={self.cep}, cidade={self.cidade}, bairro={self.bairro}, rua={self.rua}, numero={self.numero}, complemento={self.complemento})"

