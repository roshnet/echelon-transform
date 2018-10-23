
from app import app
from flask import render_template
from flask import request

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')


@app.route('/input')
def get_input():
	return render_template('input.html')


@app.route('/handle_input', methods=['GET', 'POST'])
def handle_input():
	if request.method == 'POST':
		labels, values = [], []
		for key in request.form.keys():
			labels.append(key)
		for val in request.form.values():
			values.append(val)

		return render_template('output.html', labels=labels, values=values)
	else:
		return 'You are not using HTTP POST method.'