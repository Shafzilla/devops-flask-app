#!/bin/bash

echo "Updating system."
sudo apt update -y
sudo apt upgrade -y


cd /home/vagrant
echo "Working directory set to $(pwd)"

echo "Installing required packages."

sudo apt install -y nano vim python-is-python3 python3-venv python3-pip


python -m venv .venv
echo "Virtual environment created."



echo "Installing flask into virtual environment."

/home/vagrant/.venv/bin/pip install flask



echo "Starting Flask app"

/home/vagrant/.venv/bin/python -m flask --app /vagrant/hello.py run --host=0.0.0.0 --port=5000 > /home/vagrant/flask.log 2>&1 &

echo "Script complete. Flask server is running ."
