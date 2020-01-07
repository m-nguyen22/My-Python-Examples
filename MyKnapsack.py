# Author: Minh Nguyen
# 0-1 Knapsack
# This module implements a dynamic programming solution to the 0-1 Knapsack problem

import random

class Knapsack:
	'''
	This class implements an dynamic programming solution to the 0-1 Knapsack problem
	w is a sorted list of tuples (weight, value) of available items.
	k is the carrying capacity of the knapsack
	items is a list which contains the index of items which are part of the solution
	solution is an integer value of the 

	ex.
	ks = Knapsack(21, [(4, 11), (4, 5), (6, 11)])
	print(ks)
	>>>output
	> ------------------------------------------------------
	> 
	> Knapsack max = 21
	> Item Weights, Values = [(4, 11), (4, 5), (6, 11)]
	> Max Value solution = 27
	> Items in solution include:
	> 3 (weight = 6, value = 11)
	> 2 (weight = 4, value = 5)
	> 1 (weight = 4, value = 11)
	'''

	def __init__(self, w: list, k: int):
		for i in w:
			if not isinstance(i[0], int) or not isinstance(i[1], int) or i[0] < 1 or i[0] < 1:
				raise ValueError("w contains an invalid element. Elements must be integers greater than 0")
		self.w = sorted(w, key = (lambda x: x[0]))
		self.k = k
		self.items = []
		self.solution = 0
		self.solve()

	def solve(self):
		m = [[0 for i in range(len(self.w) + 1)] for i in range(self.k + 1)]
		items = [[0 for i in range(len(self.w) + 1)] for i in range(self.k + 1)]
		for i in range(1, self.k + 1):
			for j in range(1, len(self.w) + 1):
				if i < self.w[j - 1][0]:
					m[i][j] = m[i][j - 1]
					items[i][j] = items[i][j - 1]
				else:
					# To allow multiples of the same item, m[i - self.w[j - 1][0]][j - 1] => m[i - self.w[j - 1][0]][j]
					if m[i][j - 1] > (m[i - self.w[j - 1][0]][j - 1] + self.w[j - 1][1]):
						m[i][j] = m[i][j - 1]
						items[i][j] = items[i][j - 1]
					else:
						m[i][j] = m[i - self.w[j - 1][0]][j - 1] + self.w[j - 1][1]
						items[i][j] = j
		temp = []
		curr = items[-1][-1]
		i, j = -1, -1
		while curr > 0:
			temp.append(curr)
			i -= self.w[curr - 1][0]
			j = curr - 1
			curr = items[i][j]
		self.items = temp
		self.solution = m[-1][-1]

	def __str__(self):
		s1 = "Knapsack max = {}\nItem Weights, Values = {}\nMax Value solution = {}\n".format(self.k, self.w, self.solution)
		s2 = "Items in solution include:\n"
		s3 = "".join(map(lambda x: "{} (weight = {}, value = {})\n".format(x, self.w[x - 1][0], self.w[x - 1][1]), self.items))
		return "".join([s1, s2, s3])

def test(k = None, w = None):
	if k is None:
		k = random.randint(4, 30)
	if w is None:
		w = [0] * random.randint(3, 6)
		for i in range(len(w)):
			x = random.randint(4, 15)
			w[i] = (x, int(x * random.uniform(1.1, 3)))
	ks = Knapsack(w, k)
	print("\n------------------------------------------------------\n")
	print(ks)	


if __name__ == "__main__":
	test(21, [(4, 11), (4, 5), (6, 11)])
	test()