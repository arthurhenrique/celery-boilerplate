#!/bin/bash

cd ../server/

pipenv install
pipenv run gunicorn -c gunicorn.py server:app
cd -