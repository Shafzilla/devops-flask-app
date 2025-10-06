#!/bin/bash

echo "Updating and upgrading system."

sudo apt update

sudo apt upgrade -y

echo "System updates and upgrades completed successfully."

echo "installing  python package manager."

sudo apt install -y nano vim python-is-python3 \
          python3-venv python3-pip

python -m venv .my_venv

source .my_venv/bin/activate

echo "installing flask."

pip install flask

export FLASK_APP=hello.py

nohup flask run --host=0.0.0.0 --port=5000 &

echo "script complete."


