from flask_restful import Resource

class IndexResource(Resource):
    def get(self):
        aplicacao = {'versao': '1.0'}
        return aplicacao