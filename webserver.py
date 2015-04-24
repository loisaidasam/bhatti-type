#!/usr/bin/env python

import sys

from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from gunicorn.app.base import Application

from bhattitype import BhattiType

HOST = 'localhost' # Local
#HOST = '0.0.0.0' # World available
PORT = 8052
WORKERS = 1

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


def rungunicorn():
	class WSGIServer(Application):
		def init(self, parser, opts, args):
			return {
				'bind': '%s:%s' % (HOST, PORT),
				'workers': WORKERS,
				#'errorlog': LOGFILE,
			}
		def load(self):
			return app
	#sys.argv = [sys.argv[0]]
	WSGIServer().run()

def main():
	if len(sys.argv) >= 2 and sys.argv[1] == 'test':
		print "Running in debug mode at %s on port %s" % (HOST, PORT)
		app.debug = True
		app.run(host=HOST, port=PORT)
		return

	print "Running with gunicorn at %s on port %s" % (HOST, PORT)
	rungunicorn()


if __name__ == "__main__":
	main()
