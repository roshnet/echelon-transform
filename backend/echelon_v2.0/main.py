from logic import logic
from dublicate import dublicate
from dublicate import intialize
matrix=[]
l2=[]
def entry1():
	while True:
		try:
			m=int(input("enter number of rows >>>  \n"))
			n=int(input("enter number of columns >>>  \n"))
			break
		except ValueError:
			print("please enter integer type value only")
	return m,n
def entry2(m,n,matrix):
    matrix = intialize(m,n,matrix)
    for i in range (m):
        for j in range (n):
            print ('entry in row: ',i+1,' column: ',j+1)
            while True:
            	try:
            		matrix[i][j] = float(input())
            		break
            	except ValueError:
            		print("no special characters are allowed \nplease enter valid float or integer type value")
    return matrix
m,n=entry1()
mat = entry2(m,n,matrix)
l2 = intialize(m,n,l2)
l2 = dublicate(m,n,mat,l2)
ans = logic(m,n,l2)
print(ans)
