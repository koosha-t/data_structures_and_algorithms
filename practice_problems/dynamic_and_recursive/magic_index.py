'''

Magic Index:

	A  magic index in an array A[0...n-1] is defined to be an index such that A[i]=i. Given a sorted array of distinct integer,
	write a method to find a magic index, if one exists, in Array A.

'''


def magicIndex(A, start, end):
	
	if(start > end):
		return None
	else:	
		mid = start + (end - start) // 2
		if A[mid] == mid:
			return mid
		else:
			leftMagicInd = magicIndex(A, start, mid-1)
			if leftMagicInd!=None:
				return leftMagicInd
			else:
				return magicIndex(A, mid+1, end)





### Test ###
A = [1,2,3,4,4,5]

m = magicIndex(A,0,5)

print(m)