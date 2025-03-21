# from flask_restful import fields
# from sqlalchemy import ForeignKey, Date
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from helpers.database import db

# vermifugacao_fields = {
#     'id': fields.String,
#     'nome_produto': fields.String,
#     'data_aplicacao': fields.Date,
#     'proxima_dose': fields.Date,

#     'animal_id': fields.String
# }

# class Vermifugacao(db.Model):
#     __tablename__ = 'vermifugacao'
    
#     id: Mapped[str] = mapped_column(primary_key=True)
#     nome_produto: Mapped[str] = mapped_column()
#     data_aplicacao: Mapped[Date] = mapped_column(Date)
#     proxima_dose: Mapped[Date] = mapped_column(Date)
    
#     animal_id: Mapped[str] = mapped_column(ForeignKey('animal.id'))
#     animal: Mapped["Animal"] = relationship(back_populates="vermifugacoes")

#     def __init__(self, nome_produto, data_aplicacao, proxima_dose, animal_id):
#         self.nome_produto = nome_produto
#         self.data_aplicacao = data_aplicacao
#         self.proxima_dose = proxima_dose
#         self.animal_id = animal_id

#     def __repr__(self):
#         return f"Vermifugacao(produto={self.nome_produto}, data_aplicacao={self.data_aplicacao}, proxima_dose={self.proxima_dose}, animal_id={self.animal_id})"