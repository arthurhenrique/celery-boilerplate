# -*- coding: utf-8 -*-

import gunicorn
from bottle import default_app, error, request, response, route, run
import time


@route('/salad', method='POST')
def salad():

    data = request.json
    log.info('%s' % data)

    # async calls to process that's blocker or demands high processing
    async_process()

    log.info('%s' % response.status)
    log.info('%s' % response.status_code)

    return response.status


if __name__ == "__main__":
    run(host="localhost", port=8080)

app = default_app()
