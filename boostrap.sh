#!/bin/sh
set -e pipefail

. venv/bin/activate

pip install -r requirements.txt

flask db migrate
flask db upgrade
flask run

