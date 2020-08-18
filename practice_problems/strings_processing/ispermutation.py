### Given two striings, wriite a method to decide if one is a permutation of the other ###

from collections import Counter

def isPermutation(str1, str2):
	return Counter(str1) == Counter(str2)


# Test: 

test_cases = [("abcd","cdba"),("abbc","abcc")]

for a,b in test_cases:
	print("{0} is {1} permutaton of {2}".format(a, "a" if isPermutation(a,b) else "not a" ,b))


