import random


class Snake:

	def __init__(self, x_boundary, y_boundary, x_value , y_value, size = 10):
		self.x = x_value
		self.y = y_value
		self.x_boundary = x_boundary
		self.y_boundary = y_boundary
		self.size = size

	def move(self, x, y):
		self.x += x
		self.y += y

	def boundary_colliding(self):
		if self.x < self.size or self.x > self.x_boundary - self.size:
			return True
		elif self.y < self.size or  self.y > self.y_boundary - self.size:
			return True
		return False


class Food(Snake):

	def __init__(self, x_boundary, y_boundary, size = 5):
		self.x = random.randint(10,x_boundary-10)
		self.y = random.randint(10,y_boundary-10)
		self.x_boundary = x_boundary
		self.y_boundary = y_boundary
		self.size = size

