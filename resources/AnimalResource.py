from flask_restful import marshal, marshal_with, Resource, reqparse
from helpers.database import db
from datetime import datetime
from models.Tutor import Tutor
from models.Animal import Animal, animal_fields

class AnimalResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('nome', required=True, type=str, help="Nome do animal é obrigatório.")
        self.parser.add_argument('dataNascimento', required=True, type=str, help="Data de nascimento do animal é obrigatória (formato: YYYY-MM-DD).")
        self.parser.add_argument('especie', required=True, type=str, help="Espécie do animal é obrigatória.")
        self.parser.add_argument('raca', required=True, type=str, help="Raça do animal é obrigatória.")
        self.parser.add_argument('peso', required=True, type=float, help="Peso do animal é obrigatório.")
        self.parser.add_argument('porte', required=True, type=str, help="Porte do animal é obrigatório.")
        self.parser.add_argument('pelagem', required=True, type=str, help="Pelagem do animal é obrigatória.")
        self.parser.add_argument('cadastro', required=True, type=str, help="Cadastro do animal é obrigatório.")
        # self.parser.add_argument('foto', required=True, type=str, help="Foto do animal inválida.")

    def get(self, tutor_id):
        tutor = Tutor.query.get(tutor_id)
        if not tutor:
            return {'Error': 'Tutor não encontrado'}, 404
        
        animais_table = Animal.query.filter_by(tutor_id=tutor_id).all()
        return marshal(animais_table, animal_fields), 200

    def post(self, tutor_id):
        args = self.parser.parse_args()
        try:
            tutor = Tutor.query.get(tutor_id)
            if not tutor:
                return {'Error': 'Tutor não encontrado'}, 404
            
            dataNascimento = datetime.strptime(args['dataNascimento'], "%Y/%m/%d").date()
            new_animal = Animal(
                nome=args['nome'],
                # dataNascimento=args['dataNascimento'],
                dataNascimento=dataNascimento,
                especie=args['especie'],
                raca=args['raca'],
                peso=args['peso'],
                porte=args['porte'],
                pelagem=args['pelagem'],
                cadastro=args['cadastro'],
                tutor_id=tutor.id
            )

            db.session.add(new_animal)
            db.session.commit()

            return marshal(new_animal, animal_fields), 201

        except Exception as e:
            db.session.rollback()
            return {'Error': str(e)}, 500

class AnimalByIdResource(Resource):
    def __init__(self):
        pass

    def get(self, tutor_id, pet_id):
        pass

    def put(self, pet_id):
        pass

    def delete(self):
        pass
