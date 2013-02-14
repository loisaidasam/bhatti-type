
from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request

from bhattitype import BhattiType

PORT = 8080
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

if __name__ == "__main__":
	app.debug = True
	app.run(host="0.0.0.0", port=PORT)
