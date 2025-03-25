from flask_restful import marshal, marshal_with, Resource, reqparse
from helpers.database import db
from helpers.logging import logger
from models.Vacina import Vacina, vacina_fields
from datetime import datetime

class VacinaResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('nome_vacina', required=True, type=str, help="Nome da vacina inválido.")
        self.parser.add_argument('fabricante', required=True, type=str, help="Fabricante inválido.")
        self.parser.add_argument('data_validade', required=True, type=str, help="Data de validade inválida (formato: YYYY-MM-DD).")
        self.parser.add_argument('lote', required=True, type=str, help="Lote inválido.")

    def get(self):
        try:
            logger.info("GET /vacinas - Listando todas as vacinas.")
            vacinas = Vacina.query.all()
            return marshal(vacinas, vacina_fields), 200
        except Exception as err:
            logger.error("Erro ao listar vacinas")
            return {'Error': str(err)}, 500

    @marshal_with(vacina_fields)
    def post(self):
        args = self.parser.parse_args()
        logger.info("POST /vacinas - Cadastrando nova vacina.")
        try:
            dataValidade = datetime.strptime(args['data_validade'], "%Y-%m-%d").date()
            nova_vacina = Vacina(
                nome_vacina=args['nome_vacina'],
                fabricante=args['fabricante'],
                data_validade=dataValidade,
                lote=args['lote']
            )

            db.session.add(nova_vacina)
            db.session.commit()
            logger.info("Vacina cadastrada com sucesso.")

            return nova_vacina, 201
        except Exception as err:
            db.session.rollback()
            logger.error("Erro ao cadastrar vacina.")
            return {'Error': str(err)}, 500

class VacinaByIdResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('nome_vacina', required=True, type=str, help="Nome da vacina inválido.")
        self.parser.add_argument('fabricante', required=True, type=str, help="Fabricante inválido.")
        self.parser.add_argument('data_validade', required=True, type=str, help="Data de validade inválida. (formato: YYYY-MM-DD).")
        self.parser.add_argument('lote', required=True, type=str, help="Lote inválido.")

    def get(self, vacina_id):
        try:
            logger.info(f"GET /vacinas/{vacina_id} - Listando vacina ID {vacina_id}")
            vacina = Vacina.query.get(vacina_id)

            if not vacina:
                logger.warning(f"Vacina {vacina_id} não encontrada.")
                return {"Message": "Vacina não encontrada"}, 404
            
            return marshal(vacina, vacina_fields), 200
        except Exception as err:
            logger.error("Erro ao listar vacina")
            return {'Error': str(err)}, 500

    @marshal_with(vacina_fields)
    def put(self, vacina_id):
        args = self.parser.parse_args()
        logger.info(f"PUT /vacinas/{vacina_id} - Atualizando vacina ID {vacina_id}")

        try: 
            nova_vacina = Vacina.query.get(vacina_id)
            if not nova_vacina:
                logger.warning(f"Vacina {vacina_id} não encontrada.")
                return {"Message": "Vacina não encontrada"}, 404
            
            dataValidade = datetime.strptime(args['data_validade'], "%Y-%m-%d").date()
            nova_vacina.nome_vacina = args['nome_vacina']
            nova_vacina.fabricante = args['fabricante']
            nova_vacina.data_validade = dataValidade
            nova_vacina.lote = args['lote']

            db.session.commit()
            logger.info(f"Vacina {vacina_id} atualizada com sucesso.")
            return nova_vacina, 200
        
        except Exception as err:
            db.session.rollback()
            logger.error("Erro ao atualizar vacina")
            return {'Error': str(err)}, 500


    def delete(self, vacina_id):
        try:
            logger.info(f"DELETE /vacina/{vacina_id} - Deletando vacina")
            vacina = Vacina.query.get(vacina_id)
            if not vacina:
                logger.warning(f"Vacina {vacina_id} não encontrada.")
                return {"Message": "Vacina não encontrada"}, 404
                    
            db.session.delete(vacina)
            db.session.commit()
            logger.info("Vacina deletada com sucesso.")
            return {"Sucesso": f"Vacina {vacina_id} foi deletada"}, 200
        except Exception as err:
            logger.error("Erro ao deletar vacina.")
            return {'Error': str(err)}, 500