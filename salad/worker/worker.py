# -*- coding: utf-8 -*-

from celery import Celery, Task
import time
from log import log, GraylogFilter

broker = 'amqp://localhost:5672/'
app = Celery('high_processing', broker=broker)

class HighProcessingTask(Task):

    abstract = True

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        key_tracker = args[0]

        log.addFilter(GraylogFilter(key_tracker))

        log.info('before process')

        # Simulates high processing
        time.sleep(5)
        log.info('after process')
        
        return True


@app.task(name='high_processing', base=HighProcessingTask)
def high_processing(key_tracker):
    return True