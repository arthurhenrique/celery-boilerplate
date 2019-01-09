# -*- coding: utf-8 -*-

import logging
import uuid


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()

# create formatter and add it to the handlers
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)

log.addHandler(stream_handler)
