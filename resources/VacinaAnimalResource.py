from flask_restful import marshal, Resource, reqparse
from helpers.database import db
from helpers.logging import logger
from datetime import datetime
from models.Vacina_Animal import vacina_animal_fields, Vacina_Animal
from models.Animal import Animal
from models.Vacina import Vacina

class VacinaAnimalResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('data_aplicacao', required=True, type=str, help="Data de aplicação inválida (formato: YYYY-MM-DD).")
        self.parser.add_argument('proxima_dose', required=True, type=str, help="Próxima dose inválida (formato: YYYY-MM-DD).")
        self.parser.add_argument('animal_id', required=True, type=int, help="ID do animal é obrigatório.")
        self.parser.add_argument('vacina_id', required=True, type=int, help="ID da vacina é obrigatório.")

    def get(self):
        try:
            logger.info(f"GET /registros - Listando vacinas aplicadas.")
            registros = Vacina_Animal.query.all()
            return marshal(registros, vacina_animal_fields), 200
        except Exception as err:
            logger.error("Erro ao listar vacinas aplicadas")
            return {'Error': str(err)}, 500


    def post(self):
        try:
            logger.info(f"POST /registros - Cadastrando nova aplicação de vacina.")
            args = self.parser.parse_args()

            dataAplicacao = datetime.strptime(args['data_aplicacao'], "%Y-%m-%d").date()
            proximaDose = datetime.strptime(args['proxima_dose'], "%Y-%m-%d").date()

            animal = Animal.query.get(args['animal_id'])
            vacina = Vacina.query.get(args['vacina_id'])

            if not animal or not vacina:
                logger.warning("Animal ou Vacina não encontrado.")
                return {"Error": "Animal ou Vacina não encontrados"}, 404
            
            nova_aplicação = Vacina_Animal(
                data_aplicacao=dataAplicacao,
                proxima_dose=proximaDose,
                animal_id=args['animal_id'],
                vacina_id=args['vacina_id']
            )

            db.session.add(nova_aplicação)
            db.session.commit()
            logger.info("Registro cadastrado com sucesso.")

            return marshal(nova_aplicação, vacina_animal_fields), 201
        
        except Exception as err:
            db.session.rollbak()
            logger.error("Erro ao cadastrar registro de aplicação de vacina")
            return {"Error": str(err)}, 500
        
class VacinaAnimalByAnimalResource(Resource):
    
    def get(self, animal_id):
        try:
            logger.info(f"GET /animais/{animal_id}/vacinas - Listando vacinas aplicadas no pet {animal_id}.")
            animal = Animal.query.get(animal_id)
            if not animal:
                logger.warning(f"Animal {animal_id} não encontrado.")
                return {"error": "Animal não encontrado"}, 404
            
            return marshal(animal.vacinas, vacina_animal_fields), 200
        except Exception as err:
            logger.error("Erro ao listar vacinas aplicadas no pet")
            return {"Error": str(err)}, 500
        
class VacinaAnimalByVacinaResource(Resource):

    def get(self, vacina_id):
        try:
            logger.info(f"GET /vacinas/{vacina_id}/registros - Listando registros de aplicação de vacina")
            vacina = Vacina.query.get(vacina_id)
            if not vacina:
                logger.warning(f"Vacina {vacina_id} não encontrada.")
                return {'Error': "Vacina não encontrada"}, 404
            
            return marshal(vacina.registros, vacina_animal_fields), 200
        
        except Exception as err:
            logger.error("Erro ao listar registros de aplicações de vacina")
            return {"Error": str(err)}, 500