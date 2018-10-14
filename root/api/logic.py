matrix=[]
l2=[]
m=int(input("enter number of rows >>>  \n"))
n=int(input("enter number of columns >>>  \n"))
for i in range(0,m):
    matrix.append([])
    for j in range(0,n):
        matrix[i].append(0)
for i in range (0,m):
    for j in range (0,n):
        print ('entry in row: ',i+1,' column: ',j+1)
        matrix[i][j] = float(input())
l2=matrix
print(l2)
# print (matrix)
# for i in range(m):
# 	for j in range(n):
# 		l2[i][j]=matrix[i][j]

for l in range(m):
	for i in range(l,m):
		if l2[i][j]!=0:
			for j in range(n-1,0,-1):
				l2[i][j]=l2[i][j]/l2[i][l]
		else:
			for k in range(i+1,n):
				if l2[k][l]!=0:
					for j in range(l,n):
						d=l2[i][j]
						l2[i][j]=l2[k][j]
						l2[k][j]=d
						break
			if l2[i][l]!=0:
				for j in range(n-1,l+1,-1):
					l2[i][j]=l2[i][j]/l2[i][l]
	for i in range(l+1,m):
		for j in range(l,n):
			if l2[i][j]!=0:
				l2[i][j]=l2[i][j]-l2[l][j]

print("Echelon form of \n " , matrix ,"\n is " , l2)