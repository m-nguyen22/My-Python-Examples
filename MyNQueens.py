# Author: Minh Nguyen
# This module implements a solver which finds the solutions to N-Queens

class NQueens:
	'''
	This module implements a solver which finds the solutions to N-Queens using recursive backtracking
	Boards are implemented using a 1-dimensional array, where the index is the row and
		the element is an integer representing which column a queen is at.
	
	n is the number of queens and size of board (n x n)
	col is the board
	solutions is the list of boards that are valid solutions

	ex.
	q = NQueens(4)
	print(q)
	>>>output
	> Solution 1
	> -Q--
	> ---Q
	> Q---
	> --Q-
	> Solution 2
	> --Q-
	> Q---
	> ---Q
	> -Q--
	'''

	def __init__(self, n: int):
		if n < 4:
			raise ValueError("n must be greater than 3")
		else:
			self.solutions = []
			self.col = [0] * (n + 1)
			self.n = n
			self.solve()

	def promising(self, value, index):
		for i in range(1, index):
			if self.col[i] == value or ((i + self.col[i]) == (value + index)) or ((self.col[i] - i) == (value - index)):
				return False
		return True

	def solve(self, index = 1):
		for i in range(1, self.n + 1):
			prom = self.promising(i, index)
			if not prom:
				continue
			elif index == self.n:
				self.col[index] = i
				# print("Set {} as {}, and appending {}".format(index, i, self.col))
				self.solutions.append(self.col.copy())
			else:
				self.col[index] = i
				# print("Set {} as {}".format(index, i))
				self.solve(index + 1)

	def __str__(self):
		string = ""
		for num, sol in enumerate(self.solutions, start = 1):
			
			string = string + ("Solution {}\n".format(num))
			sol = ["".join(["-" * (x - 1), "Q", "-" * (self.n - x), "\n"]) for x in sol]
			string = "".join([string, "".join(sol[1:]), "\n"])

			# it = iter(sol)
			# next(it)
			# for i in it:
			# 	s = "".join(["-" * (i - 1), "Q", "-" * (self.n - i), "\n"])
			# 	string = "".join([string, s])
		return string

def testnqueens(n: int):
	test = NQueens(n)
	print(test)

if __name__ == "__main__":
	for i in range(4, 7):
		print("Testing {}-Queens".format(i))
		testnqueens(i)