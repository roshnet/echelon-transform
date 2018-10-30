

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


@app.route('/handle_input', methods=['POST'])
def handle_input():
	if request.method == 'POST':
		keys, values = [], []
		data = request.form
		for key in data.keys():
			keys.append(key)
		for val in data.values():
			values.append(int(val))

		# Targeting the 6th and 8th char in the last element in the list 'keys',
		# as the last element's name tells number of rows and columns.
		m = int(keys[len(keys)-1][5]) 
		n = int(keys[len(keys)-1][7])

		# Now traversing over the entries in the list 'values', and generating
		# a regular 2D matrix from it based on the keynames.

		matrix = []
		idx = 0

		while idx < (m*n):
			row = []
			for x in range(n):
				# runs <# of columns> times, always.
				row.append(values[idx+x])
			matrix.append(row)
			idx = idx + n
		matrix_tmp = deepcopy(matrix)
		matrix_conv = convert(matrix_tmp)

		return render_template('output.html', matrix_orig=matrix, matrix_conv=matrix_conv)

	else:
		return 'You are not using HTTP POST method.'


if __name__ == '__main__':
	app.run(debug=True)