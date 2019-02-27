#!/bin/bash

cd ../worker/

pipenv install
pipenv run celery -E -A worker:app worker --loglevel=INFO -c 20
cd -