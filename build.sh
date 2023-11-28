#!/usr/bin/env bash
# exit on error
set -o errexit

#poetry install
#pip install -r requerements.txt

python manage.py collectstatic --no-input
python manage.py migrate