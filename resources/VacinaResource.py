from flask_restful import marshal, marshal_with, Resource, reqparse
from helpers.database import db
from models.Vacina import Vacina, vacina_fields
#from models.VacinaAnimal import VacinaAnimal, vacina_animal_fields
#from datetime import datetime

class VacinaResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('nome_vacina', required=True, type=str, help="Nome da vacina inválido.")
        self.parser.add_argument('fabricante', required=True, type=str, help="Fabricante inválido.")
        self.parser.add_argument('data_validade', required=True, type=str, help="Data de validade inválida.")
        self.parser.add_argument('lote', required=True, type=str, help="Lote inválido.")

    def get(self):
        try:
            vacinas = Vacina.query.all()
            return marshal(vacinas, vacina_fields), 200
        except Exception as err:
            return {'Error': str(err)}, 500

    @marshal_with(vacina_fields)
    def post(self):
        args = self.parser.parse_args()
        
        try:
            nova_vacina = Vacina(
                nome_vacina=args['nome_vacina'],
                fabricante=args['fabricante'],
                data_validade=args['data_validade'],
                lote=args['lote']
            )

            db.session.add(nova_vacina)
            db.session.commit()

            return nova_vacina, 201
        except Exception as err:
            db.session.rollback()
            return {'Error': str(err)}, 500

class VacinaByIdResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('nome_vacina', required=True, type=str, help="Nome da vacina inválido.")
        self.parser.add_argument('fabricante', required=True, type=str, help="Fabricante inválido.")
        self.parser.add_argument('data_validade', required=True, type=str, help="Data de validade inválida.")
        self.parser.add_argument('lote', required=True, type=str, help="Lote inválido.")

    def get(self, vacina_id):
        try:
            vacina = Vacina.query.get(vacina_id)

            if not vacina:
                return {"Message": "Vacina não encontrada"}, 404
            
            return marshal(vacina, vacina_fields), 200
        except Exception as err:
            return {'Error': str(err)}, 500

    @marshal_with(vacina_fields)
    def put(self, vacina_id):
        args = self.parser.parse_args()

        # try:
        #     data_validade = datetime.strptime(args['data_validade'], "%d/%m/%Y").date()
        # except ValueError:
        #     return {"message": "Data de validade inválida. Use o formato dd/mm/aaaa."}, 400


        try: 
            nova_vacina = Vacina.query.get(vacina_id)
            if not nova_vacina:
                return {"Message": "Vacina não encontrada"}, 404
            
            nova_vacina.nome_vacina = args['nome_vacina']
            nova_vacina.fabricante = args['fabricante']
            nova_vacina.data_validade = args['data_validade']
            nova_vacina.lote = args['lote']

            db.session.commit()
            
            return nova_vacina, 200
        
        except Exception as err:
            db.session.rollback()
            return {'Error': str(err)}, 500


    def delete(self, vacina_id):
        try:
            vacina = Vacina.query.get(vacina_id)
            if not vacina:
                return {"Message": "Vacina não encontrada"}, 404
                    
            db.session.delete(vacina)
            db.session.commit()
            return {"Sucesso": f"Vacina {vacina_id} foi deletada"}, 200
        except Exception as err:
            return {'Error': str(err)}, 500