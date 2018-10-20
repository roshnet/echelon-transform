def logic(m,n,l2):
	j = 0
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
	return l2
	