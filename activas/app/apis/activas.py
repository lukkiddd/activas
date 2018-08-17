from flask_restplus import Namespace, Resource


api = Namespace('activas', description='Activas API')


@api.route('/')
class Activas(Resource):
    def get(self):
        return {
            "message": "Hello Activas!"
        }
