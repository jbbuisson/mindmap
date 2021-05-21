# TODO readme

import json

from flask import Flask, request
from markupsafe import escape

import mindmap

app = Flask(__name__)

@app.route("/mindmap", methods=['GET', 'POST'])
def mindmap_api():
    data = json.loads(request.data)
    id = escape(data.get("id"))
    if request.method == 'POST':
        mindmap.createMap(id)
        return '', 200
    else:
        return mindmap.pretty_print_map(id, False), 200


@app.route("/leaf/<map_id>", methods=['GET', 'POST'])
def leaf_api(map_id):
    data = json.loads(request.data)
    path = str(escape(data.get("path")))
    text = str(escape(data.get("text")))

    if request.method == 'POST':
        mindmap.add_nodes(map_id, path, text)
        return '', 200
    else:
        return mindmap.get_leaves(map_id, path), 200


if __name__ == '__main__':
    app.run()
