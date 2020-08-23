'''

Write a method to sort an array of strings so that all the anagrams are next to each other

'''

from collections import Counter

def anagram(s):
	return frozenset(tuple(Counter(s).items()))


def groupAnagram(words):
	anagDic = {}

	for word in words:
		w_anag = anagram(word)
		if w_anag in anagDic:
			anagDic[w_anag].append(word)
		else:
			anagDic[w_anag] = list()
			anagDic[w_anag].append(word)

	groups =  list(anagDic.values())

	return [item for group in groups for item in group]



input = ["abc","dda","bac","ijk","dad","abc",'kji']

print("grouping anagrams for list {0}:\n{1}".format(input ,groupAnagram(input)))


