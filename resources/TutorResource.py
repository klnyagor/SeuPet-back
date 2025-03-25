from flask_restful import marshal, marshal_with, Resource, reqparse
from helpers.database import db
from helpers.logging import logger
from models.Tutor import Tutor, tutor_fields
from models.Endereco import Endereco


class TutorResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('nome', required=True, type=str, help="Nome inválido.")
        self.parser.add_argument('email', required=True, type=str, help='Email inválido.')
        self.parser.add_argument('documento', required=True, type=str, help="Documento de identificação inválido.")
        self.parser.add_argument('estado', required=True, type=str, help="Estado inválido.")
        self.parser.add_argument('cep', required=True, type=str, help="CEP inválido.")
        self.parser.add_argument('cidade', required=True, type=str, help="Cidade inválida.")
        self.parser.add_argument('bairro', required=True, type=str, help="Bairro inválido.")
        self.parser.add_argument('rua', required=True, type=str, help="Rua inválida.")
        self.parser.add_argument('numero', required=True, type=int, help="Número inválido.")
        self.parser.add_argument('complemento', required=True, type=str, help="Complemento inválido.")


    def get(self):
        try:
            logger.info("GET /tutores - Listando os tutores")
            tutores_table = Tutor.query.all()
            return marshal(tutores_table, tutor_fields), 200
        except Exception as err:
            logger.error(f"Erro ao listar tutores: {str(err)}")
            return {'Error': str(err)}, 500
        
    @marshal_with(tutor_fields)
    def post(self):
        logger.info("POST /tutores - Criando novo tutor")
        args = self.parser.parse_args()
        try:

            new_endereco = Endereco(
                estado=args['estado'],
                cep=args['cep'],
                cidade=args['cidade'],
                bairro=args['bairro'],
                rua=args['rua'],
                numero=args['numero'],
                complemento=args['complemento']
            )

            db.session.add(new_endereco)
            db.session.flush()

            new_tutor = Tutor(
                nome= args['nome'],
                email= args['email'],
                documento= args['documento'],
                endereco_id=new_endereco.id
            )

            db.session.add(new_tutor)
            db.session.commit()
            logger.info(f"Tutor criado com sucesso: ID {new_tutor.id}")

            return new_tutor, 201
        except Exception as err:
            logger.error(f"Erro ao criar tutor: {str(err)}")
            db.session.rollback()
            return {'Error': str(err)}, 500
        
class TutorByIdResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('nome', required=True, type=str, help="Nome inválido.")
        self.parser.add_argument('email', required=True, type=str, help='Email inválido.')
        self.parser.add_argument('documento', required=True, type=str, help="Documento de identificação inválido.")
        self.parser.add_argument('estado', required=True, type=str, help="Estado inválido.")
        self.parser.add_argument('cep', required=True, type=str, help="CEP inválido.")
        self.parser.add_argument('cidade', required=True, type=str, help="Cidade inválida.")
        self.parser.add_argument('bairro', required=True, type=str, help="Bairro inválido.")
        self.parser.add_argument('rua', required=True, type=str, help="Rua inválida.")
        self.parser.add_argument('numero', required=True, type=int, help="Número inválido.")
        self.parser.add_argument('complemento', required=True, type=str, help="Complemento inválido.")
        

    def get(self, tutor_id):
        try:
            tutor = Tutor.query.get(tutor_id)
            logger.info(f"GET /tutores/{tutor_id} - Listando o tutor: ID {tutor_id}")

            if not tutor:
                logger.warning(f"Tutor ID {tutor_id} não foi encontrado.")
                return {"Message": "Tutor não encontrado."}, 404
            
            return marshal(tutor, tutor_fields), 200
        except Exception as err:
            logger.error(f"Erro ao listar tutor: ID {tutor_id}")
            return {'Error': str(err)}, 500
        
    def delete(self, tutor_id):
        try:
            logger.info(f"DELETE /tutores/{tutor_id} - Deletando o tutor: ID {tutor_id}")
            tutor = Tutor.query.get(tutor_id)
            if not tutor:
                logger.warning(f"Tutor ID {tutor_id} não foi encontrado.")
                return {"Message": "Tutor não encontrado"}, 404
                
            db.session.delete(tutor)
            db.session.commit()
            logger.info("Tutor deletado com sucesso.")
            return {"Sucesso": f"Tutor foi deletado"}, 200
        except Exception as err:
            logger.error("Erro ao deletar tutor.")
            return {'Error': str(err)}, 500
    
    @marshal_with(tutor_fields)
    def put(self, tutor_id):
        args = self.parser.parse_args()
        logger.info(f"PUT /tutores/{tutor_id} - Atualizando o tutor: ID {tutor_id}")
        try: 
            tutor = Tutor.query.get(tutor_id)
            if not tutor:
                logger.warning(f"Tutor ID {tutor_id} não foi encontrado.")
                return {"Message": "Tutor não encontrado"}, 404
            
            endereco = tutor.endereco
            
            tutor.nome = args['nome']
            tutor.email = args['email']
            tutor.documento = args['documento']
            endereco.estado = args['estado']
            endereco.cep = args['cep']
            endereco.cidade = args['cidade']
            endereco.bairro = args['bairro']
            endereco.rua = args['rua']
            endereco.numero = args['numero']
            endereco.complemento = args['complemento']

            db.session.commit()
            logger.info("Tutor atualizado com sucesso.")
            
            return tutor, 200
        
        except Exception as err:
            logger.error("Erro ao tentar atualizar tutor")
            db.session.rollback()
            return {'Error': str(err)}, 500

