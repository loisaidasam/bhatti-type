#!/usr/bin/env python

import os
import sys

from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request

from bhattitype import BhattiType


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/api/", methods=['GET', 'POST'])
def api():
    bt = BhattiType()
    if request.method == 'POST':
        input = request.form.get('text', '')
    else:
        input = request.args.get('text', '')
    output = bt.convert(input)
    return jsonify({'status': 'OK', 'input': input, 'output': output})


def main():
    HOST = os.environ.get('HOST') or 'localhost'
    PORT = int(os.environ.get('PORT') or 8052)
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print "Debug mode!"
        app.debug = True
    print "Running at %s on port %s" % (HOST, PORT)
    app.run(host=HOST, port=PORT)


if __name__ == "__main__":
    main()
