from flask_restful import Api
from resources.IndexResource import IndexResource
from resources.TutorResource import TutorResource, TutorByIdResource
from resources.AnimalResource import AnimalResource, AnimalByIdResource

api = Api(prefix="/api")

api.add_resource(IndexResource, '/')
api.add_resource(TutorResource, '/tutores')
api.add_resource(TutorByIdResource, '/tutores/<int:tutor_id>')


api.add_resource(AnimalResource, '/tutores/<int:tutor_id>/animais')
api.add_resource(AnimalByIdResource, '/tutores/<int:tutor_id>/animais/<int:pet_id>')
# api.add_resource(AnimalResource, '/animais')
# api.add_resource(AnimalByIdResource, '/animais/<int:pet_id>')
