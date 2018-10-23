

from flask import Flask
from flask import render_template, request
from copy import deepcopy
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
		data = request.form
		for key in data.keys():
			keys.append(key)
		for val in data.values():
			values.append(int(val))

		m = int(keys[len(keys)-1][5]) ## when name="elem-m-n"
		# m = keys[len(keys)-1][0] ## when name="m-n"

		n = int(keys[len(keys)-1][7])
		matrix = []
		idx = 0
		while idx < (m*n):
			for x in range(n):
				# runs <# of columns> times, always.
				row = []
				row.append(values[idx+x])
			matrix.append(row)
			idx = idx + n
		matrix_tmp = deepcopy(matrix)
		matrix_conv = convert(matrix_tmp)
		del matrix_tmp
		# matrix prepared after above 'while' finishes..
		# print('\n\n', data, '\n\n', m, '\n\n', n, '\n\n')
		print('\n\n', matrix, '\n\n')
		print('\n', matrix_conv, '\n\n')
		print('\n\n\n')
		return render_template('output.html', original=matrix, converted=matrix_conv)

	else:
		return 'You are not using HTTP POST method.'


if __name__ == '__main__':
	app.run(debug=True)