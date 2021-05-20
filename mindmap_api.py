# TODO readme

from flask import Flask, request
from flask_restful import Api, Resource, abort
from marshmallow import Schema, fields

import mindmap

class MindMapQuerySchema(Schema):
    id = fields.Str(required=True)

app = Flask(__name__)
api = Api(app)
mindmapQuerySchema = MindMapQuerySchema()

class MindMap(Resource):
    def post(self):
        errors = mindmapQuerySchema.validate(request.args)
        if errors:
            abort(400, str(errors))

        mindmap.createMap(request.args['id'])
        return '', 200

    def get(self):
        errors = mindmapQuerySchema.validate(request.args)
        if errors:
            abort(400, str(errors))

        mindmap.pretty_print_map(request.args['id'], False)
        return '', 200

class LeafQuerySchemaPost(Schema):
    id = fields.Str(required=True)
    path = fields.Str(required=True)
    text = fields.Str(required=True)

class LeafQuerySchemaGet(Schema):
    id = fields.Str(required=True)
    path = fields.Str(required=True)

leafQuerySchemaPost = LeafQuerySchemaPost()
leafQuerySchemaGet = LeafQuerySchemaGet()

class Leaf(Resource):
    def post(self):
        errors = leafQuerySchemaPost.validate(request.args)
        if errors:
            abort(400, str(errors))

        mindmap.add_nodes(request.args['id'], request.args['path'], request.args['text'])
        return '', 200

    def get(self):
        errors = leafQuerySchemaGet.validate(request.args)
        if errors:
            abort(400, str(errors))

        return mindmap.get_leaves(request.args['id'], request.args['path']), 200

api.add_resource(MindMap, '/mindmap')
api.add_resource(Leaf, '/leaf')

if __name__ == '__main__':
    app.run()
