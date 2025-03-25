from flask_restful import Api
from resources.IndexResource import IndexResource
from resources.TutorResource import TutorResource, TutorByIdResource
from resources.AnimalResource import AnimalResource, AnimalByIdResource, AnimalResourceAllTutor, AnimalByIdResourceAllTutor
from resources.VacinaResource import VacinaResource, VacinaByIdResource
from resources.VacinaAnimalResource import VacinaAnimalResource, VacinaAnimalByAnimalResource, VacinaAnimalByVacinaResource

api = Api(prefix="/api")

api.add_resource(IndexResource, '/')
api.add_resource(TutorResource, '/tutores')
api.add_resource(TutorByIdResource, '/tutores/<int:tutor_id>')


api.add_resource(AnimalResource, '/tutores/<int:tutor_id>/animais')
api.add_resource(AnimalByIdResource, '/tutores/<int:tutor_id>/animais/<int:pet_id>')
api.add_resource(AnimalResourceAllTutor, '/animais')
api.add_resource(AnimalByIdResourceAllTutor, '/animais/<int:pet_id>')


api.add_resource(VacinaResource, '/vacinas')
api.add_resource(VacinaByIdResource, '/vacinas/<int:vacina_id>')


api.add_resource(VacinaAnimalResource, '/registros')
api.add_resource(VacinaAnimalByAnimalResource, '/animais/<int:animal_id>/vacinas')
api.add_resource(VacinaAnimalByVacinaResource, '/vacinas/<int:vacina_id>/registros')