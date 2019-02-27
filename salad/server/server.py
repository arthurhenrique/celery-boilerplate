# -*- coding: utf-8 -*-

import time

from flask import Flask, Response, jsonify, request

from log import log
from process import async_process

app = Flask(__name__)

@app.route('/salad', methods=['POST'])
def salad():
    data = request.json
    log.info(f"{data}")

    # async calls to process that's blocker or demands high processing
    async_process()

    return jsonify({"http": 200})


if __name__ == "__main__":
    app.run()
