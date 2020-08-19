### Write an algorithm such that if an element in an M*N matrix is 0, its entire row and column are set to 0 ####


def zeroMatrix(mat):
	r,c = mat.shape[0], mat.shape[1]

	for i in range(r):
		for j in range(c):
			if mat[i][j]==0:
				mat[i, list(range(c))] =0
				mat[list(range(r)), j] = 0

	return mat



### test
