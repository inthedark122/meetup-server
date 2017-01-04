from api import api_blueprint

from flask import Flask


app = Flask(__name__)
app.register_blueprint(api_blueprint)


def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
