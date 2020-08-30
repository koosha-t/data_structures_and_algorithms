### The maximum subarray problem is a task to find the series of contiguous elements with the maximum sum in any given array.

def maxSubArray(arr):
	maxSum = [0] * len(arr)
	maxSum[0] = arr[0]
	start = end = 0

	for i in range(1,len(arr)):
		maxSum[i] = max(maxSum[i-1]+arr[i], arr[i])
		start = i if arr[i] >  maxSum[i-1] + arr[i] else start


	return max(maxSum), start, maxSum.index(max(maxSum))



print(maxSubArray([-3,1,-8,4,-1,2,1,-5,5]))
			

