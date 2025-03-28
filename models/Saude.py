# from flask_restful import fields
# from sqlalchemy import ForeignKey, Text
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from helpers.database import db

# saude_fields = {
#     'id': fields.String,
#     'alergias': fields.String,
#     'medicamentos': fields.String,
#     'observacoes': fields.String
# }

# class Saude(db.Model):
#     __tablename__ = 'saude'
    
#     id: Mapped[str] = mapped_column(primary_key=True)
#     alergias: Mapped[str] = mapped_column(Text)
#     medicamentos: Mapped[str] = mapped_column(Text)
#     observacoes: Mapped[str] = mapped_column(Text)
    
#     animal_id: Mapped[str] = mapped_column(ForeignKey('animal.id'))
#     animal: Mapped["Animal"] = relationship(back_populates="saude")

#     def __init__(self, alergias, medicamentos, observacoes, animal_id):
#         self.alergias = alergias
#         self.medicamentos = medicamentos
#         self.observacoes = observacoes

#         self.animal_id = animal_id

#     def __repr__(self):
#         return f"Saude(alergias={self.alergias}, medicamentos={self.medicamentos}, observacoes={self.observacoes}, animal_id={self.animal_id})"
