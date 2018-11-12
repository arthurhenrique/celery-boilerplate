# -*- coding: utf-8 -*-

import time
from celery import Celery
from log import log

def async_process(key_tracker):
    
    rabbit_path = 'amqp://guest:guest@127.0.0.1:5672/'
    app = Celery('high_processing', broker=rabbit_path)
    log.info(key_tracker)

    result = app.send_task('high_processing', arg=key_tracker)
    
    log.info('%s' % result)

    return True
