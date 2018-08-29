import json
import os
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
        dir_path = os.path.dirname(os.path.realpath(__file__))
        data_path = os.path.join(dir_path, '../data/dataset01.json')
        with open(data_path) as f:
            data = json.load(f)
        return data


@api.route('/save')
class Save(Resource):
    def post(self):
        return {}