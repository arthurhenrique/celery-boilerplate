# -*- coding: utf-8 -*-

from celery import Celery, Task
import time
from config import data
from log import log

broker = (
    data["rabbitmq"]["protocol"]
    + "://"
    + data["rabbitmq"]["ip"]
    + ":"
    + data["rabbitmq"]["port"]
)


app = Celery('high_processing', broker=broker)


class HighProcessingTask(Task):

    abstract = True

    def after_return(self, status, retval, task_id, args, kwargs, einfo):

        log.info('before process')

        # Simulates high processing
        time.sleep(5)
        log.info('after process')

        return True


@app.task(name='high_processing', base=HighProcessingTask)
def high_processing():
    return True
