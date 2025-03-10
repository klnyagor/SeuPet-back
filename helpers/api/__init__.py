from flask_restful import Api
from resources.IndexResource import IndexResource

api = Api(prefix="/api")

api.add_resource(IndexResource, '/')