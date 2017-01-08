from api.restplus import api

from api.parsers import pagination_arguments

from .serializers import report_post_model, report_response_model, report_list_model
from .business import create_report, delete_report, update_report

from database.models import Report

from flask import request
from flask_restplus import Resource

ns = api.namespace('reports', description='Reports')

@ns.route('')
class ReportCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(report_list_model)
    def get(self):
        """
        Get all reports by page
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        reports = Report.query.paginate(page, per_page, error_out=False).items

        return {'reports': reports}

    @api.expect(report_post_model)
    @api.marshal_with(report_response_model)
    def post(self):
        """
        Update report
        """
        report = create_report(request.json)

        return {'report': report}

@ns.route('/<int:id>')
@api.doc(params={'id': 'Report id'})
@api.response(404, 'Report not found.')
class ReportItem(Resource):

    @api.marshal_with(report_response_model)
    def get(self, id):
        """
        Get report by id
        """
        report = Report.query.filter(Report.id == id).one()

        return {'report': report}

    @api.expect(report_post_model)
    @api.marshal_with(report_response_model)
    def put(self, id):
        """
        Update report
        """
        report = update_report(id, request.json)

        return {'report': report}

    @api.response(204, 'Report successfully deleted.')
    def delete(self, id):
        """
        Delete report
        """

        delete_report(id)
        return None, 204

