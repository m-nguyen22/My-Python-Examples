# Author: Minh Nguyen
# This module contains two sorting algorithms methods, implemented in Python.

def Swap(ls: list, i1: int, i2: int):
	temp = ls[i1]
	ls[i1] = ls[i2]
	ls[i2] = temp
	return ls

def Heapify(ls: list, end):
	j = end // 2
	for i in range(end, j - 1, -1):
		k = i
		while k != 0:
			parent = (k - 1) // 2
			if(ls[k] > ls[parent]):
				ls = Swap(ls, k, parent)
			k = parent
	return ls

def MyHeapSort(ls: list, k = None):
	'''
	This heapsort takes a list and sorts it using a max heap.
	It takes two parameters:
	ls (the list being sorted)
	k (an integer for where the algorithm to stop sorting. This will default to the full array.)
	'''
	if not isinstance(ls, list):
		raise TypeError('Input param was not a list.')
	if len(ls) == 0:
		raise ValueError('Input list is length 0.')
	if k == None:
		k = len(ls) - 1
	for i in range(k, 0, -1):
		ls = Heapify(ls, i)
		ls = Swap(ls, 0, i)
	return ls

def MyMergeSort(ls: list, i = None, j = None):
	'''
	This mergesort takes a list and sorts it using recursive calls to mergesort.
	It takes three parameters:
	ls (the list being sorted)
	i (the first element to start the sort. This will default to 0, the first element if not specified.)
	j (the last element to end the sort. This will default to the end of the list if not specified.)
	'''
	if not isinstance(ls, list):
		raise TypeError('Input param was not a list.')
	if len(ls) == 0:
		raise ValueError('Input list is length 0.')
	if i == None:
		i = 0
	if j == None:
		j = len(ls) - 1

	if((j - i + 1) > 1):
		mid = (j + i) // 2
		left = iter(MyMergeSort(ls, i, mid))
		right = iter(MyMergeSort(ls, mid + 1, j))
		l = next(left)
		r = next(right)

		ls = []
		while True:
			try:
				if l < r:
					ls.append(l)
					l = None
					l = next(left)
				else:
					ls.append(r)
					r = None
					r = next(right)
			except:
				if isinstance(l, int):
					ls.append(l)
					left = list(left)
					ls.extend(left)
				else:
					ls.append(r)
					right = list(right)
					ls.extend(right)
				break
		return ls
	else:
		return [ls[i]]
					

if __name__ == '__main__':
	test_arrs = [
		[1, 5, 3, 6, 7, 8, 2000, 30, 500],
		[1],
		[1000, -23, 39, 45],
		[390, 89, 3]
	]
	for array in test_arrs:
		array = MyMergeSort(array)
		print(array)
	for array in test_arrs:
		array = MyHeapSort(array)
		print(array)
		
