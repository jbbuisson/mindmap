from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

import mindmap

app = Flask(__name__)
api = Api(app)

class MindMap(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize

        parser.add_argument('id', required=True)

        args = parser.parse_args()  # parse arguments to dictionary
        mindmap.createMap(args.id)
        return '', 200

    def get(self):
        # data = pd.read_csv('users.csv')  # read CSV
        # data = data.to_dict()  # convert dataframe to dictionary
        # return {'data': data}, 200  # return data and 200 OK code
        parser = reqparse.RequestParser()  # initialize

        parser.add_argument('id', required=True)

        args = parser.parse_args()  # parse arguments to dictionary
        mindmap.prettyPrintMap(args.id, False)
        return '', 200

class Leaf(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize

        parser.add_argument('id', required=True)
        parser.add_argument('path', required=True)
        parser.add_argument('text', required=True)

        args = parser.parse_args()  # parse arguments to dictionary
        mindmap.addNodes(args.id, args.path, args.text)
        return '', 200

    def get(self):
        parser = reqparse.RequestParser()  # initialize

        parser.add_argument('id', required=True)
        parser.add_argument('path', required=True)

        args = parser.parse_args()  # parse arguments to dictionary
        
        return mindmap.getLeaves(args.id, args.path), 200

api.add_resource(MindMap, '/mindmap')  # '/users' is our entry point
api.add_resource(Leaf, '/leaf')  # '/users' is our entry point

if __name__ == '__main__':
    app.run(debug = True)