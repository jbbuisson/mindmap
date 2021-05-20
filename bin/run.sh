#!/bin/sh
pip3 install virtualenv
python3 -m virtualenv ./.venv
source ./.venv/bin/activate
python mindmap_api.py