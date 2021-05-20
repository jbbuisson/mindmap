#!/bin/sh
VIRTUAL_ENV=./.venv
pip3 install virtualenv
python3 -m virtualenv $VIRTUAL_ENV
. $VIRTUAL_ENV/bin/activate
pip install -r requirements.txt
python mindmap_api.py