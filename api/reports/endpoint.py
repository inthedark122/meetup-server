from api.restplus import api
from api.parsers import pagination_arguments

from flask_restplus import Resource

ns = api.namespace('reports', description='Reports')

@ns.route('/')
class ReportCollection(Resource):

    @api.expect(pagination_arguments)
    def get(self):
        return {
            'reports': []
        }

