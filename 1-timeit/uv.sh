#!/bin/sh
uv venv $1
. $1/bin/activate
uv pip install -r requirements.txt
deactivate