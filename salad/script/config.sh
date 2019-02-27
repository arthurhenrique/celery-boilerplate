#!/bin/bash

# configure .env file to address IP
echo "configuring .env docker"
REMOTE_ADDR=$(hostname -I | awk '{print $1}')

grep "$REMOTE_ADDR" .env

echo "STEP .env"
sed -ri -e  "s/REMOTE_ADDR=.*$/REMOTE_ADDR=$REMOTE_ADDR/" .env
grep -n $REMOTE_ADDR .env


echo "bye!"