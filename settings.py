import os

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql+pg8000://meetup_user:qwerty@localhost/meetup_develop')
SQLALCHEMY_TRACK_MODIFICATIONS = False
RESTPLUS_VALIDATE = True
