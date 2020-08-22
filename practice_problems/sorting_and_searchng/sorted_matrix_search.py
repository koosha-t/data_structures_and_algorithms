'''

Given an M*N matrix in which each row and each column is sorted in ascending order ,write a method to find an element

'''


import numpy as np 

#finding x in 1-d array
def binary_search(x ,arr, start, end):
	if(start>end):
		return None
	mid = start + ((end - start) // 2)
	if arr[mid] == x:
		return mid
	elif arr[mid] < x:
		return binary_search(x, arr, mid+1, end)
	else:
		return binary_search(x, arr, start, mid -1)


#Finding the row in M which may contain value x
def get_row(x, first_col, start_row, end_row):
	if start_row > end_row:
		return None

	elif start_row == end_row:
		return start_row

	else:
		mid_row = start_row + ((end_row - start_row) // 2)
		if first_col[mid_row] <= x and mid_row<len(first_col)-1 and first_col[mid_row+1] > x:
			return mid_row

		elif first_col[mid_row] > x:
			return get_row(x, first_col, start_row, mid_row-1)
		else:
			return get_row(x, first_col, mid_row+1, end_row)




#  Finding x in a sorted matrix M
def mat_search(x,M):
	first_col = M[:,0].reshape(1,-1)[0]
	row = get_row(x, first_col, 0, len(first_col)-1)
	col = binary_search(x, M[row], 0, len(M[row])-1)
	if row==None or col==None:
		return None
	return (row, col)


ar = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

print("array:\n{}\n".format(ar))
print("{0} is located at {1}".format(7,mat_search(7,ar)))
print("{0} is located at {1}".format(10,mat_search(10,ar)))
print("{0} is located at {1}".format(4,mat_search(4,ar)))
print("{0} is located at {1}".format(12,mat_search(12,ar)))
print("{0} is located at {1}".format(1,mat_search(1,ar)))
print("{0} is located at {1}".format(15,mat_search(15,ar)))
print("{0} is located at {1}".format(0,mat_search(0,ar)))




