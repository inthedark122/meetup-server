import settings

from api import api_blueprint
from database import db

from flask import Flask


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['RESTPLUS_VALIDATE'] = True

app.register_blueprint(api_blueprint)
db.init_app(app)

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
