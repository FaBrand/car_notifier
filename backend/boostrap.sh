#!/bin/bash
set -e pipefail

source venv/bin/activate

pip install -r requirements.txt

flask db init
flask db migrate
flask db upgrade

