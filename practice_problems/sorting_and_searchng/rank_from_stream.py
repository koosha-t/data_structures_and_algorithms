'''


Imagine you are reading in a stream of integers. Periodically, you wish to be able to look up the rank of a 
number x (the number of values less than or equal to x). Write a method which is called when each number is generated, 
whiich returns the number of values less than or equal to x (not inicluding x itself)


'''


class BST:

	def __init__(self, data):
		self.data = data
		self.left_child = None
		self.right_child = None
		self.leftCount = 0
		self.rightCount = 0


	def add(self, newData):
		if newData <= self.data:
			self.leftCount+=1
			if self.left_child == None:
				self.left_child  = BST(newData)
				if self.data == newData:
					return 1
				else:
					return 0
			elif self.data == newData:
				return 1+ self.left_child.add(newData)	
			else:
				return self.left_child.add(newData)
			
		else:
			self.rightCount+=1
			if self.right_child == None:
				self.right_child = BST(newData)
				return self.leftCount + 1
			else:
				return self.leftCount + 1 +self.right_child.add(newData)


input = [1,4,4,5,9,7,13,3]
bst = BST(5)
for x in input:
	print("adding {0}, rank: {1}".format(x,bst.add(x)))
			
