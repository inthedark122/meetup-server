from api.restplus import api
from api.reports.endpoint import ns as reports_namespace

from flask import Blueprint

api_blueprint = Blueprint('api', __name__, url_prefix='/api')
api.init_app(api_blueprint)

api.add_namespace(reports_namespace)
