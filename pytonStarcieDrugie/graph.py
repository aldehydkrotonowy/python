class Graph(object):
	def __init__(self, graph_dict=None):
		if graph_dict == None:
			graph_dict = {}
		self.graphDict = graph_dict
	def vertices(self):
		return list(self.graphDict.keys())
	def edges(self):
		return self.generateEdges()
	def add_vertex(self, vertex):
		if vertex not in self.graphDict:
			self.graphDict[vertex] = []
	def add_edge(self, edge):
		edge = set(edge)
		(vertex1, vetrex2) = tuple(edge)
		if vertex1 in self.graphDict:
			self.graphDict[vertex1].append(vetrex2)
		else:
			self.graphDict[vertex1] = vetrex2
	def generateEdges(self):
		edges = []
		for vertex in self.graphDict:
			for neighbour in self.graphDict[vertex]:
				if {neighbour, vertex} not in edges:
					edges.append({vertex, neighbour})
		return edges
	def toString(self):
		res = 'vertex: '
		for k in self.graphDict:
			res += str(k) + ' '
		res +='\nedges: '
		for edges in self.generateEdges():
			res += str(edges) + ' '
		return res
	

if __name__ == "__main__":
	g = {"a" : ["d"],
		 "b" : ["c"],
		 "c" : ["b", "c", "d", "e"],
		 "d" : ["a", "c"],
		 "e" : ["c"],
		 "f" : []
		}


	graph = Graph(g)

	print("Vertices of graph:")
	print(graph.vertices())
	print('edges')
	print(graph.edges())
	print("Add vertex:")
	graph.add_vertex("z")
	print("Vertices of graph:")
	print(graph.vertices()) 
	print("Add an edge:")
	graph.add_edge({"a","z"})
	print("Vertices of graph:")
	print(graph.vertices())
	print("Edges of graph:")
	print(graph.edges())
