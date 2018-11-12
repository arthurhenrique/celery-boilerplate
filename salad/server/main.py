# -*- coding: utf-8 -*-

from process import async_process
from bottle import run, response, request, route
from log import log, GraylogFilter
import time

@route('/salad', method='POST')
def salad():
    graylog = GraylogFilter()
    log.addFilter(graylog)

    data = request.json
    log.info('%s' % data)

    # async calls to process that's blocker or demands high processing
    async_process(graylog.key_tracker)

    log.info('%s' % response.status)
    log.info('%s' % response.status_code)

    return response.status

run(server='bjoern', host='0.0.0.0', port=8080, debug=True)
