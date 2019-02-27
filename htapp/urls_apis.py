from flask_restful import Api
from .apis import *
api = Api()
def init_api(app):
    api.init_app(app)

api.add_resource(RegisterAPI, "/api/regisyer")
api.add_resource(ItemAPI,'/api/item')

