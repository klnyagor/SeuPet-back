from flask_restful import fields
from sqlalchemy import ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from helpers.database import db
from models.DateField import DateField
from models.Animal import animal_fields
from models.Vacina import vacina_fields

vacina_animal_fields = {
    'id': fields.Integer,
    'data_aplicacao': DateField(attribute='data_aplicacao'),
    'proxima_dose': DateField(attribute='proxima_dose'),

    'animal': fields.Nested(animal_fields),
    'vacina': fields.Nested(vacina_fields)
}

class Vacina_Animal(db.Model):
    __tablename__ = 'vacina_animal'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    data_aplicacao: Mapped[Date] = mapped_column(Date)
    proxima_dose: Mapped[Date] = mapped_column(Date)
    
    animal_id: Mapped[int] = mapped_column(ForeignKey('animal.id'))
    animal: Mapped["Animal"] = relationship(back_populates="vacinas")

    vacina_id: Mapped[int] = mapped_column(ForeignKey('vacina.id'))
    vacina: Mapped["Vacina"] = relationship(back_populates="registros")

    def __init__(self, data_aplicacao, proxima_dose, animal_id, vacina_id):
        self.data_aplicacao = data_aplicacao
        self.proxima_dose = proxima_dose

        self.animal_id = animal_id
        self.vacina_id = vacina_id

    def __repr__(self) -> str:
        return f"Vacina_Animal(data_aplicacao={self.data_aplicacao}, proxima_dose={self.proxima_dose}, animal_id={self.animal_id}, vacina_id={self.vacina_id})"
