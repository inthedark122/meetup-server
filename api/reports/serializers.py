from api.restplus import api
from flask_restplus import fields

report_model_updater = api.model('Report model update', {
    'title': fields.String(attribute='title', required=True, description='Report title', allow_null=False),
    'description': fields.String(attribute='description', required=False, description='Report description', allow_null=False)
})

report_model = api.inherit('Report model', report_model_updater, {
    'id': fields.Integer(attribute='id', readOnly=True, description='The unique identifier of a report'),
    
})

report_post_model = api.model('Report save model', {
    'report': fields.Nested(report_model, required=True)
})

report_list_model = api.model('Report list', {
    'reports': fields.List(fields.Nested(report_model, required=True))
})
