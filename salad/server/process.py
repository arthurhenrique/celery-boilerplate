# -*- coding: utf-8 -*-

import time
from celery import Celery
from config import data
from log import log


def async_process():

    rabbit_path = (
        data["rabbitmq"]["protocol"]
        + "://"
        + data["rabbitmq"]["user"]
        + ":"
        + data["rabbitmq"]["pwd"]
        + "@"
        + data["rabbitmq"]["ip"]
        + ":"
        + data["rabbitmq"]["port"]
        + "/"
    )

    app = Celery('high_processing', broker=rabbit_path)

    result = app.send_task('high_processing')

    log.info(f"{result}")

    return True
