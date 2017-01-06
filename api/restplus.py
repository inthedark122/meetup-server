from flask_restplus import Api
from sqlalchemy.orm.exc import NoResultFound


api = Api(
    version='0.1.0',
    title='Meetup',
    description='Confiration'
)

@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'

    return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    message = 'A database result was required but none was found.'

    return {'message': message}, 404