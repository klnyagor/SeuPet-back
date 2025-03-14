from flask_restful import fields
from sqlalchemy import ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from helpers.database import db

vacina_fields = {
    'id': fields.String,
    'nome_vacina': fields.String,
    'data_aplicacao': fields.Date,
    'proxima_dose': fields.Date,

    'animal_id': fields.String
}

class Vacina(db.Model):
    __tablename__ = 'vacina'
    
    id: Mapped[str] = mapped_column(primary_key=True)
    nome_vacina: Mapped[str] = mapped_column()
    data_aplicacao: Mapped[Date] = mapped_column(Date)
    proxima_dose: Mapped[Date] = mapped_column(Date)
    
    animal_id: Mapped[str] = mapped_column(ForeignKey('animal.id'))
    animal: Mapped["Animal"] = relationship(back_populates="vacinas")

    def __init__(self, nome_vacina, data_aplicacao, proxima_dose, animal_id):
        self.nome_vacina = nome_vacina
        self.data_aplicacao = data_aplicacao
        self.proxima_dose = proxima_dose

        self.animal_id = animal_id

    def __repr__(self) -> str:
        return f"Vacina(vacina={self.nome_vacina}, data_aplicacao={self.data_aplicacao}, proxima_dose={self.proxima_dose}, animal_id={self.animal_id})"
