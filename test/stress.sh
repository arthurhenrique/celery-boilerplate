#!/bin/bash

while [ true ]; 
do 
	curl -X POST  http://127.0.0.1:8080/salad -H 'Content-Type: application/json' -H 'Postman-Token: 237cf3e4-3b37-405e-ae96-1611881d447e' -H 'cache-control: no-cache' -d '{"ingredients": ["cucumber","celery", "radish"]}';
done

