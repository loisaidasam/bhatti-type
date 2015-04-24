#!/usr/bin/env python

import logging
import os
import sys

from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request

from bhattitype import BhattiType


app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/api/", methods=['GET', 'POST'])
def api():
    bt = BhattiType()
    params = request.method == 'POST' and request.form or request.args
    q = params.get('q') or ''
    logger.info("q: %s", q)
    result = bt.convert(q)
    return jsonify({'status': 'OK', 'q': q, 'result': result})


def main():
    HOST = os.environ.get('HOST') or 'localhost'
    PORT = int(os.environ.get('PORT') or 8052)
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        logger.warning("Debug mode!")
        app.debug = True
    logger.info("Running at %s on port %s", HOST, PORT)
    app.run(host=HOST, port=PORT)


if __name__ == "__main__":
    main()
