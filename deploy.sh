#!/bin/bash

echo "base configuration"
./config.sh

echo "docker configuration"
docker swarm init

echo "docker-compose build"
docker-compose build

echo "docker deploy"
docker stack rm cucumber
sleep 20
docker stack deploy -c docker-compose-prod.yml cucumber
if [ $? -ne 0 ];then
    echo "docker stack deploy -c docker-compose-prod.yml cucumber"
fi
