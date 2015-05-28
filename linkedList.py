class Node:

	def __init__(self, initdata):
		self.data = initdata
		self.next = None

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_data(self, new_data):
		self.data =new_data

	def set_next(self, next_node):
		self.next = next_node

first = Node(10)
second = Node(2)
first.set_next(2)

print first.get_next()