from flask import Blueprint
from flask_restplus import Api
from .activas import api as activas

blueprint = Blueprint('api', __name__, url_prefix='/api')


@blueprint.after_request
def add_header(response):
    prefix = 'Access-Control-Allow'
    response.headers[f'{prefix}-Headers'] = 'Content-Type,Authorization'
    response.headers[f'{prefix}-Methods'] = 'GET, PUT, POST, DELETE, OPTIONS'
    response.headers[f'{prefix}-Origin'] = '*'
    return response


api = Api(
    blueprint,
    title='Activas',
    version='1.0',
    description='Activas API',
    doc='/documentation'
)

api.add_namespace(activas)
