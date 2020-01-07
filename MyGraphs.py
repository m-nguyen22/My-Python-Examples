# Author: Minh Nguyen
# This module contains graph classes, including the base data structure and some graph algorithms.

from collections import deque
import random

class UnweightedGraph:
	'''
	This class provides structure for an unweighted graph.
	Vertices is a list of 'nodes'.
	Edges is a map of 'nodes' to a set of other 'nodes'.
	Directed is a boolean value instructing whether or not the graph is directed. This defaults to False.
	'''

	def __str__(self):
		v = str(self.vertices)
		e = str(self.edges)
		return ("Vertices = {}\nEdges = {}".format(v, e))

	def __init__(self, vertices: list, edges: list, directed: bool):
		self.vertices = vertices
		self.edges = {}
		for v in vertices:
			self.edges[v] = set()
		self.directed = directed
		for i in edges:
			try:
				self.addedges(i[0], i[1])
			except ValueError as error:
				print(error)
				continue

	def addvertex(self, x):
		if not x in self.vertices:
			self.vertices.append(x)
			self.edges[x] = set()
		else:
			print("Vertex is already in the graph")

	def addedges(self, x, y):
		if x == y:
			raise ValueError("Edge could not be added: source and destination and the same")
		# Cases
		# If we don't enforce adding the vertex first:
		#	One or both vertices are missing (need to add them)
		#	Vertices are added, but the set in the edge dict is missing (should always create set when adding a vertex)
		#	Vertices are added, but the edge is not there (normal)
		# If we enforce adding the vertex, we only need to worry about the third.
		if not x in self.vertices or not y in self.vertices:
			raise ValueError("An input vertex is not in graph")
		self.edges[x].add(y)
		if not self.directed:
			self.edges[y].add(x)

	def findpath(self, x, y):
		# BFS for finding the shortest path from x to y.

		if not x in self.vertices or not y in self.vertices:
			raise ValueError("An input vertex is not in the graph")

		nearest = {}
		visited = set([x])
		queue = deque([])
		queue.append(x)

		# Search for paths to y until one is found
		while queue:
			curr = queue.popleft()
			if curr == y:
				break
			else:
				edges = self.edges[curr]
				edges = edges.difference(visited)
				for i in edges:
					visited.add(i)
					queue.append(i)
					nearest[i] = curr

		# Given the nearest dict, build a path list.
		if y not in nearest:
			print("No path from {} to {}".format(x, y))
		else:
			path = deque([])
			curr = y
			while curr != x:
				path.appendleft(curr)
				curr = nearest[curr]
			path.appendleft(curr)
			return list(path)

def test(v = None, e = None, w = False, s = 0, d = -1):
	if v is None:
		v = []
		for i in range(7):
			v.append(i)
	if e is None:
		e = []
		for i in range(30):
			r = (v[random.randint(0,6)], v[random.randint(0,6)])
			e.append(r)
	ug = UnweightedGraph(v, e, w)
	print(ug)
	print(ug.findpath(v[s], v[d]))


if __name__ == "__main__":
	v = ['A', 'B', 'C', 'D']
	e = [('A', 'C'), ('B', 'C'), ('A', 'B'), ('C', 'D')]
	v2 = [1, 2, 3, 4, 5]
	e2 = [(1, 2),(1, 4),(2, 3),(4, 5),(2, 4),(3, 4),(3, 5)]
	test(v, e, False)
	test(v2, e2, False)
	test()