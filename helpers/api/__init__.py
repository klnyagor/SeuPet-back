from flask_restful import Api
from resources.IndexResource import IndexResource
from resources.TutorResource import TutorResource, TutorByIdResource

api = Api(prefix="/api")

api.add_resource(IndexResource, '/')
api.add_resource(TutorResource, '/tutores')
api.add_resource(TutorByIdResource, '/tutores/<int:tutor_id>')
