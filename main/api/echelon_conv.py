

def convert(arr):
	# 'arr' is a 2D array, or a list of lists.
	# Assuming fake logic, viz to add 100 to every element of 'matrix'.
	for i in range(len(arr)):
		for ii in range(len(arr[0])):
			arr[i][ii] = arr[i][ii] + 100
	return arr