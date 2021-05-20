# TODO readme

from flask import Flask
from flask_restful import Api, Resource, reqparse

import mindmap

app = Flask(__name__)
api = Api(app)

class MindMap(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('id', required=True)

        args = parser.parse_args()  # parse arguments to dictionary
        mindmap.createMap(args.id)
        return '', 200

    def get(self):
        parser = reqparse.RequestParser()

        parser.add_argument('id', required=True)

        args = parser.parse_args()  # parse arguments to dictionary
        mindmap.prettyPrintMap(args.id, False)
        return '', 200

class Leaf(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('id', required=True)
        parser.add_argument('path', required=True)
        parser.add_argument('text', required=True)

        args = parser.parse_args()  # parse arguments to dictionary
        mindmap.addNodes(args.id, args.path, args.text)
        return '', 200

    def get(self):
        parser = reqparse.RequestParser()

        parser.add_argument('id', required=True)
        parser.add_argument('path', required=True)

        args = parser.parse_args()  # parse arguments to dictionary

        return mindmap.getLeaves(args.id, args.path), 200

api.add_resource(MindMap, '/mindmap')
api.add_resource(Leaf, '/leaf')

if __name__ == '__main__':
    app.run(debug = True)
