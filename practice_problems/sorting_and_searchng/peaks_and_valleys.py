'''

In an array of integes, a peak is an element whicih is greater than or equal to the adjacent integers and a valley is an
element which is less than or equal to the adjacent integes. For example, ini the array {5,8,6,2,3,4,6}, {8,6} are peaks
and {5,2} are valleys. Given an array of integers, sort the array into an alternating sequence of peaks and valleys

Example:
input: {5,3,1,2,3}
output:{5,1,3,2,3}

'''


#approach 1: using sort,O(nlogn)

def pv(input):
	sorted_input = sorted(input)
	output  = list()
	i = 0
	j = len(input) -1
	while i<j:
		output.append(sorted_input[j])
		output.append(sorted_input[i])
		i+=1
		j-=1

	if i==j:
		output.append(sorted_input[i])	
	return output

print(pv([1,2,3,4,5,6,7,8,9]))
print(pv([5,3,1,2,3]))


#approach 2: not using sort, O(n)
def pv_helper(ind, input):
	if ind%2:
		return input.index(min(input[ind-1:ind+2]))
	else:
		if ind>0:
			return input.index(max(input[ind-1:ind+2]))
		else:
			return input.index(max(input[:ind+2])) 


def pv_linear(input):
	for i in range(len(input)):
		k = pv_helper(i, input)
		t = input[i]
		input[i] = input[k]
		input[k] = t
	return input

print(pv_linear([1,2,3,4,5,6,7,8,9]))
print(pv_linear([5,3,1,2,3]))






