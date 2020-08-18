### There are three types of edts can be performed on strings: insert a char, remove a char, or replace a char. Given
### two strings, write a functin to check if they are one edit (or zero edits) away.


def oneAway(str1, str2):
	if len(str1) == len(str2):
		dif = 0
		for i in range(len(str1)):
			if str1[i] != str2[i]:
				dif+=1
				if dif>1:
					return False
		return True

	elif abs(len(str1)- len(str2)) == 1:
		longer = str1 if len(str1)>len(str2) else str2
		shorter =  str1 if len(str1)<len(str2) else str2

		for i in range(len(longer)):
			if shorter == longer[:i] + longer[i+1:]:
				return True

		return False

	else:
		return False


pairs = [('abc','abbc'),('salam','salak'),('abcd','abbd'),('abcdef','abcdd')]

for a,b in pairs:
	print("{0} and {1} are {2} step(s) away.".format(a,b, 'only one' if oneAway(a,b) else 'more than one'))


