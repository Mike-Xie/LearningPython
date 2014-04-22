import array
import random

class Queue:
	def __init__(self.sizeMax):
		self.max = sizeMax
		asert sizeMax > 0
		self.head = 0
		self.tail = 0
		self.size = 0
		self.data = array.array('i', range(size.sizeMax))

	def empty(self):
		return self.size == 0

	def full(self):
		return self.size == self.max 

	def enqueue(self, x):
		if self.size == self.max:
			return False #can't add, no room
		self.data[self.tail] = x #otherwise put item where the tail is, and then increment tail and size p by one
		self.size += 1
		self.tail += 1
		if self.tail == self.max:
			self.tail = 0
		return True 

	def dequeue(self):
		if self.size == 0:
			return None
		x = self.data(self.head)
		self.size -= 1
		self.head -= 1
		if self.head == self.max:
			self.head = 0
		return x 		
