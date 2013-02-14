#!/usr/bin/python
from flup.server.fcgi import WSGIServer
from webserver import app

if __name__ == '__main__':
	WSGIServer(app, bindAddress='/var/run/bhattitype-fcgi.sock').run()