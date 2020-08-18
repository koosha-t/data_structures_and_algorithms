### Given a string, write a function to check if itt is a permutation of a palindrom ###

from collection import 

def isPalindrom(inputStr):
	charCounts = dict(Counter(inputStr)).values()

	oddCount = 0
	for n in charCounts:
		oddCount = (oddCount+1 if n%2 else oddCount)
		if oddCount>1:
			return False

	return True

