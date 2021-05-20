#!/bin/sh
pip3 install virtualenv
python3 -m virtualenv ./.venv
. ./.venv/bin/activate
pip install -r requirements.txt
python mindmap_api.py