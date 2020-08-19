import numpy as np 

def rotateRight(M):
	
	a,b = M.shape[0], M.shape[1]	

	r = np.zeros(shape=(b, a))

	for i in range(b):
		for j in range(a):
			r[i][j] = M[a-j-1][i]

	return r



def rotateLeft(M):
	return rotateRight(rotateRight(rotateRight(M)))

#test

ar = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

print(rotateRight(ar))

print(rotateLeft(ar))

