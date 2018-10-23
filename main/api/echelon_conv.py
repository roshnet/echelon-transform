

def convert(matrix):
	# 'matrix' is a 2D array, or a list of lists.
	# Assuming fake logic, viz to add 100 to every element of 'matrix'.
	for i in range(len(matrix)):
		for ii in range(len(matrix[0])):
			matrix[i][ii] = matrix[i][ii] + 100
	return matrix