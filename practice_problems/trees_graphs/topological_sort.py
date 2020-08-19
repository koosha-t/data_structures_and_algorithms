###################################
######### Topological Sort#########
###################################


class DirectedGraph:

	def __init__(self, nodes):
		self.nodes = nodes
		self.edges = dict.fromkeys(nodes)
		self.finishTime = dict.fromkeys(nodes)
		self.visited = set()
		self.clock = 0


	def  addEdge(self, node1, node2):
		if node1 in self.nodes and node2 in self.nodes:
			if self.edges[node1] == None:
				self.edges[node1] = set()
			self.edges[node1].add(node2)
			return True
		else:
			return False


	def dfs(self, startNode):
		self.visited.add(startNode)
		self.clock+=1
		if self.edges[startNode] != None:
			for nei in self.edges[startNode]:
				if nei not in self.visited:
					self.dfs(nei)

		self.clock+=1
		self.finishTime[startNode] = self.clock
		

	def topologicalSort(self):
		self.clock = 0
		self.visited = set()
		for n in self.nodes:
			if n not in self.visited:
				self.dfs(n)

		return sorted(self.nodes, key = lambda x: self.finishTime[x], reverse=True)
		


#### Test ####

tasks = ["undershorts", "pants","belt","shirt","tie","jacket","socks","shoes","watch"]
dg = DirectedGraph(tasks)
dg.addEdge("pants","belt")
dg.addEdge("shirt","belt")
dg.addEdge("shirt","tie")
dg.addEdge("belt","jacket")
dg.addEdge("tie","jacket")
dg.addEdge("undershorts","pants")
dg.addEdge("undershorts","shoes")
dg.addEdge("socks","shoes")
dg.addEdge("pants","shoes")


print(dg.topologicalSort())








