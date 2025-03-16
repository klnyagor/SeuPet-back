# from flask_restful import fields
# from sqlalchemy import ForeignKey, Date
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from helpers.database import db
# from models.Animal import animal_fields
# from models.Vacina import vacina_fields

# vacina_animal_fields = {
#     'id': fields.Integer,
#     'data_aplicacao': Date,
#     'proxima_dose': Date,

#     'animal': fields.Nested(animal_fields),
#     'vacina': fields.Nested(vacina_fields)
# }

# class Vacina(db.Model):
#     __tablename__ = 'vacina_animal'
    
#     id: Mapped[str] = mapped_column(primary_key=True)
#     data_aplicacao: Mapped[Date] = mapped_column(Date)
#     proxima_dose: Mapped[Date] = mapped_column(Date)
    
#     animal_id: Mapped[str] = mapped_column(ForeignKey('animal.id'))
#     animal: Mapped["Animal"] = relationship(back_populates="vacinas", cascade="all, delete-orphan")

#     vacina_id: Mapped[str] = mapped_column(ForeignKey('vacina.id'))
#     vacina: Mapped["Vacina"] = relationship(back_populates="vacina_animal")

#     def __init__(self, data_aplicacao, proxima_dose, animal_id, vacina_id):
#         self.data_aplicacao = data_aplicacao
#         self.proxima_dose = proxima_dose

#         self.animal_id = animal_id
#         self.vacina_id = vacina_id

#     def __repr__(self) -> str:
#         return f"Vacina_Animal(data_aplicacao={self.data_aplicacao}, proxima_dose={self.proxima_dose}, animal_id={self.animal_id})"
