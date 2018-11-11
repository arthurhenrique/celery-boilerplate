from process import async_process
from bottle import run, response, request, route
from log import log

@route('/salad', method='POST')
def salad():
    data = request.json
    log.info('%s' % data)
    
    # async calls to process that's blocker or demands high processing
    async_process(data)    
    
    return response.status

run(server='bjoern', host='0.0.0.0', port=8080, debug=True)
