from flask_restplus import Namespace, Resource


api = Namespace('activas', description='Activas API')


@api.route('/')
class Activas(Resource):
    def get(self):
        return {
            "message": "Hello Activas!"
        }


@api.route('/data')
class Data(Resource):
    def get(self):
        return {
            "data": []
        }


@api.route('/save')
class Save(Resource):
    def post(self):
        return {}