from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)

class MindMap(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize

        parser.add_argument('id', required=True)

        args = parser.parse_args()  # parse arguments to dictionary
        return {'action': 'POST', 'args': args}, 200

    def get(self):
        # data = pd.read_csv('users.csv')  # read CSV
        # data = data.to_dict()  # convert dataframe to dictionary
        # return {'data': data}, 200  # return data and 200 OK code
        return {'action': 'GET', 'text': 'Pretty print mindmapping'}, 200

class Leaf(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize

        parser.add_argument('path', required=True)
        parser.add_argument('text', required=True)

        args = parser.parse_args()  # parse arguments to dictionary
        return {'text': 'Add a leaf', 'args': args}

    def get(self):
        return {'text': 'Read a leaf'}

api.add_resource(MindMap, '/mindmap')  # '/users' is our entry point
api.add_resource(Leaf, '/leaf')  # '/users' is our entry point

if __name__ == '__main__':
    app.run(debug = True)