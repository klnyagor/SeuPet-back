from flask_restful import marshal, marshal_with, Resource, reqparse

from helpers.database import db

from models.Tutor import Tutor, tutor_fields

class TutorResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('nome', required=True, type=str, help="Nome inválido.")
        self.parser.add_argument('email', required=True, type=str, help='Email inválido.')
        self.parser.add_argument('documento', required=True, type=str, help="Documento de identificação inválido.")

    def get(self):
        try:
            tutores_table = Tutor.query.all()
            return marshal(tutores_table, tutor_fields), 200
        except Exception as err:
            return {'Error': str(err)}, 500
        
    @marshal_with(tutor_fields)
    def post(self):
        args = self.parser.parse_args()
        try:
            new_tutor = Tutor(
                nome= args['nome'],
                email= args['email'],
                documento= args['documento']
            )

            db.session.add(new_tutor)
            db.session.commit()

            return new_tutor, 201
        except Exception as err:
            return {'Error': str(err)}, 500
        
class TutorByIdResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('nome', required=True, type=str, help="Nome inválido.")
        self.parser.add_argument('email', required=True, type=str, help='Email inválido.')
        self.parser.add_argument('documento', required=True, type=str, help="Documento de identificação inválido.")

    def get(self, tutor_id):
        try:
            tutor = Tutor.query.get(tutor_id)

            if not tutor:
                return {"Message": "Tutor não encontrado"}, 404
            
            return marshal(tutor, tutor_fields), 200
        except Exception as err:
            return {'Error': str(err)}, 500
        
    def delete(self, tutor_id):
        try:
            tutor = Tutor.query.get(tutor_id)
            if not tutor:
                return {"Message": "Tutor não encontrado"}, 404
                
            db.session.delete(tutor)
            db.session.commit()
            return {"Sucesso": f"Tutor foi deletado"}, 200
        except Exception as err:
            return {'Error': str(err)}, 500
    
    @marshal_with(tutor_fields)
    def put(self, tutor_id):
        args = self.parser.parse_args()
        try: 
            tutor = Tutor.query.get(tutor_id)
            if not tutor:
                return {"Message": "Tutor não encontrado"}, 404
            
            tutor.nome = args['nome']
            tutor.email = args['email']
            tutor.documento = args['documento']

            db.session.commit()
            
            return tutor, 200
        
        except Exception as err:
            return {'Error': str(err)}, 500

