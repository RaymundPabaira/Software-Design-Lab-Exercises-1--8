from collections import defaultdict

class Graph:

	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self,a,b):
		self.graph[a].append(b)

	def BFS(self, jaypen):
		visited = [False] * (max(self.graph) + 1)
		queue = []
		queue.append(jaypen)
		visited[jaypen] = True

		while queue:
			jaypen = queue.pop(0)
			print (jaypen, end = " ")

			for i in self.graph[jaypen]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True

jay = Graph()
jay.addEdge(0, 1)
jay.addEdge(0, 2)
jay.addEdge(1, 2)
jay.addEdge(2, 0)
jay.addEdge(2, 3)
jay.addEdge(3, 3)

print ("The Breadth First Traversal is shown below (beginning with vertex 2): ")
jay.BFS(2)


