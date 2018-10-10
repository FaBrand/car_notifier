#!/bin/sh
set -e pipefail

. venv/bin/activate

pip install -r requirements.txt

flask init
flask migrate
flask upgrade
flask run

