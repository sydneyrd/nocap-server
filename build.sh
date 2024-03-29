#!/usr/bin/env bash

set -o errexit  # exit on error

# Install Nginx


# Install Python dependencies
pip install -r requirements.txt

# Uncomment these lines if you want to run them during deployment
python3 manage.py collectstatic --no-input
# python3 manage.py migrate
# python3 manage.py loaddata weapons.json servers.json roles.json factions.json
