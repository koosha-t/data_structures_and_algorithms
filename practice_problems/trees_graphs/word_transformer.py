'''

Given two words of equal length that are in a dictionary, write a method to 
transform one word into another word by changing onoly one letter at a time. 
The new word you get in each step must be in the dictionary.

'''


class WordTransformer:

	alphabet = 'abcdefghijklmnopqrstuvwxyz'

	def __init__(self, dictionary=None):
		self.dictionary = dictionary

	def add(self, word):
		if word not in self.dictionary:
			self.dictionary.add(word)

	# len(word) * len(alphabet)
	def _adj_words(self, word):
		adj = set()
		for i in range(len(word)):
			for ch in self.alphabet:
				if word[i] != ch:
					temp_word = word[:i] + ch + word[i+1:]
					if temp_word in self.dictionary and temp_word not in adj:
						adj.add(temp_word)
		return adj


	def transform(self, w1, w2):
		que = [w1]
		visited = set()
		visited.add(w1)
		parent = {w1:None}

		#BFS
		while len(que) > 0:
			current_word = que[0]
			que.remove(que[0])
			adj_words = self._adj_words(current_word)

			for word in adj_words:
				if word not in visited:
					parent[word] = current_word
					visited.add(word)
					que.append(word)

		if w2 in visited:
			path = [w2]
			w_i = w2
			while parent[w_i] != None:
				w_i = parent[w_i]
				path.append(w_i)
			path.reverse()
			return path
		else:
			return None



wt = WordTransformer(set(('damp','like','limp','lime','lamp','aaaa','bbbb','cccc')))

print(wt.transform('damp','like'))



