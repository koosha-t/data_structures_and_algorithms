'''

Given an N*N matrix of positive and negative integers, write code to ofind the submatrix with the largest possible sum.

'''

import numpy as np

def maxSubMatrix(arr):
	n_rows, n_cols = arr.shape
	col_sum = np.zeros(shape = arr.shape)
	max_sub = arr[0][0]

	for c in range(n_cols):
		col_sum[0][c] = arr[0][c]

		for r in range(1,n_rows):
			col_sum[r][c] = arr[r][c] + col_sum[r-1][c]

	max_start_row = max_end_row = 0

	for startRow in range(0, n_rows):
		for endRow in range(startRow, n_rows):
			partialSum = [0] * n_cols
			partialSum[0] = col_sum[endRow][0] - col_sum[startRow-1][0] if startRow > 0 else col_sum[endRow][0]
			for col in range(1, n_cols):
				if startRow > 0:
					partialSum[col] = max(col_sum[endRow][col] - col_sum[startRow-1][col] + partialSum[col-1], col_sum[endRow][col] - col_sum[startRow-1][col])
				else:
					partialSum[col] = max(col_sum[endRow][col] + partialSum[col-1], col_sum[endRow][col] )

			
			if max(partialSum) > max_sub:
				max_sub = max(partialSum)
				max_start_row = startRow
				max_end_row = endRow

	return max_sub, max_start_row, max_end_row




print(maxSubMatrix(np.array([[2,-1],[1,1]])))
print(maxSubMatrix(np.array([[2,-1,1],[3,-2,4],[-5,4,2]])))