# from flask_restful import fields
# from sqlalchemy import ForeignKey, Date, Text
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from helpers.database import db

# doenca_fields = {
#     'id': fields.String,
#     'nome_doenca': fields.String,
#     'data_diagnostico': fields.String,
#     'tratamento': fields.String,

#     'animal_id': fields.String
# }

# class Doenca(db.Model):
#     __tablename__ = 'doenca'
    
#     id: Mapped[str] = mapped_column(primary_key=True)
#     nome_doenca: Mapped[str] = mapped_column()
#     data_diagnostico: Mapped[Date] = mapped_column(Date)
#     tratamento: Mapped[str] = mapped_column(Text)
    
#     animal_id: Mapped[str] = mapped_column(ForeignKey('animal.id'))
#     animal: Mapped["Animal"] = relationship(back_populates="doencas")

#     def __init__(self, nome_doenca, data_diagnostico, tratamento, animal_id):
#         self.nome_doenca = nome_doenca
#         self.data_diagnostico = data_diagnostico
#         self.tratamento = tratamento

#         self.animal_id = animal_id

#     def __repr__(self):
#         return f"Doenca(doenca={self.nome_doenca}, data_diagnostico={self.data_diagnostico}, tratamento={self.tratamento}, animal_id={self.animal_id})"