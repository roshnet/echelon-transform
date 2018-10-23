

from flask import Flask
from flask import render_template, request

from api.echelon_conv import convert

app = Flask(__name__)

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
		keys, values = [], []
		for key in request.form.keys():
			keys.append(key)
		for val in request.form.values():
			values.append(int(val))

		m = int(keys[len(keys)-1][5]) ## when name="elem-m-n"
		# m = keys[len(keys)-1][0] ## when name="m-n"

		n = int(keys[len(keys)-1][7])
		matrix = []
		idx = 0
		while idx < (m*n):
			for _ in range(n):
				# runs <# of columns> times, always.
				row = []
				row.append(values[idx])
			matrix.append(row)
			idx = idx + n
		matrix_conv = convert(matrix)
		# matrix prepared after above 'while' finishes..
		return render_template('output.html', original=matrix, converted=matrix_conv)

	else:
		return 'You are not using HTTP POST method.'


if __name__ == '__main__':
	app.run(debug=True)