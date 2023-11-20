from website import create_app
from flask import Flask
from flask_restful import Api, Resource

appapi = Flask(__name__)
api = Api(appapi)

class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello World"}

api.add_resource(HelloWorld, "/api")

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)