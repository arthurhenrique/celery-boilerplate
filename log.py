# -*- coding: utf-8 -*-

import logging
import graypy
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

#handler = graypy.GELFHandler('localhost', 12201)
handler = graypy.GELFHandler('127.0.0.1', 12201)
handlerStream = logging.StreamHandler()

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)
handlerStream.setFormatter(formatter)

log.addHandler(handler)
log.addHandler(handlerStream)


