import os

from config import data, server_ip
from sh import celery

broker = (
    data["rabbitmq"]["protocol"]
    + "://"
    + data["rabbitmq"]["user"]
    + ":"
    + data["rabbitmq"]["pwd"]
    + "@"
    + data["rabbitmq"]["ip"]
    + ":"
    + data["rabbitmq"]["port"]
)

monit = celery(
    "flower", "--broker={}//".format(
        broker), "--port={}".format(data["flower"]["port"])
)
