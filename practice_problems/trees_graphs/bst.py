##########################
### Binary Search Tree ###
##########################

class BST_Node:
	def  __init__(self, data):
		self.data = data
		self.leftChild = None
		self.rightChild = None

	def add(self, newData):
		if newData <= self.data:
			if self.leftChild == None:
				self.leftChild = BST_Node(newData)
			else:
				self.leftChild.add(newData)
		else:
			if self.rightChild == None:
				self.rightChild = BST_Node(newData)
			else:
				self.rightChild.add(newData)

	def inOrder(self):
		if self.leftChild != None:
			self.leftChild.inOrder()

		print(self.data)

		if self.rightChild != None:
			self.rightChild.inOrder()

	def preOrder(self):
		print(self.data)
		if self.leftChild != None:
			self.leftChild.preOrder()
		if self.rightChild != None:
			self.rightChild.preOrder()


	def postOrder(self):
		if self.leftChild != None:
			self.leftChild.postOrder()
		if self.rightChild != None:
			self.rightChild.postOrder()

		print(self.data)


class BST(BST_Node):
	def __init__(self, root_data):
		BST_Node.__init__(self, root_data)


### Test

bst = BST(5)
bst.add(2)
bst.add(3)
bst.add(10)
bst.add(1)
bst.add(1.5)
bst.add(7)
bst.add(9)
bst.add(13)


print("in-order traversal:")
bst.inOrder()

print("pre-order traversal:")
bst.preOrder()

print("post-order traversal:")
bst.postOrder()










