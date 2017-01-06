from database import db
from database.models import Report

def save_report(report, data):
    report_data = data.get('report')
    report.title = report_data.get('title')
    report.description = report_data.get('description')

    db.session.add(report)
    db.session.commit()

def create_report(data):
    report = Report()
    save_report(report, data)
    return report

def update_report(report_id, data):
    report = Report.query.filter(Report.id == report_id).one()
    save_report(report, data)
    return report


def delete_report(report_id):
    report = Report.query.filter(Report.id == report_id).one()

    db.session.delete(report)
    db.session.commit()
