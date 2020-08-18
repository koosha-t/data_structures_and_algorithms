## Implement and algorithm to determine if a sttrinig has all unique chars ##

def isAllUnique(s):
	return len(set(s)) == len(s)

#test

words = [ "abcde","Koosha","XxYy"]


for w in words:
	print("{0}: {1}".format(w, isAllUnique(w)))

