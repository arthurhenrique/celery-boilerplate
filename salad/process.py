import time
import celery
from log import log
def async_process(kwargs):
    log.info('%s %s' % (__name__, kwargs))
    
    # simulates high processing
    time.sleep(10)
    
    return True

