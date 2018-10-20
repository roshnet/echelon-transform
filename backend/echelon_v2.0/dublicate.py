def dublicate(m,n,matrix,l2):
	for i in range(m):
		for j in range(n):
			l2[i][j]=matrix[i][j]
	return l2
def intialize(m,n,array):
	for i in range(m):
	    array.append([])
	    for j in range(n):
		    array[i].append(0)
	return array
