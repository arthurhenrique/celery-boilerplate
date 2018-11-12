# -*- coding: utf-8 -*-

import logging
import graypy
import uuid

class GraylogFilter(logging.Filter):
    def __init__(self, key_tracker=str(uuid.uuid4())):
        self.key_tracker = key_tracker

    def filter(self, record):
        record.key_tracker = self.key_tracker
        return True

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

gray_handler = graypy.GELFHandler('127.0.0.1', 12201)
stream_handler = logging.StreamHandler()

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
gray_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

log.addHandler(gray_handler)
log.addHandler(stream_handler)
