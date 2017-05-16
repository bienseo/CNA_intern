'''
CNA Intern
Study name: Layers - MulLayer(곱셈 노드), AddLayer(덧셈 노드)
Created by Eunseo Cho on 16/05/2017.
'''

class MulLayer:
	def __init__(self):
		self.x = None
		self.y = None

	def forward(self, x, y):
		self.x = x
		self.y = y
		out = x * y

		return out

	def backward(self, dout):
		dx = dout * self.y # switch x and y
		dy = dout * self.x

		return dx, dy

class AddLayer:
	def __init__(self):
		pass

	def forward(self, x, y):
		out = x + y

		return out

	def backward(self, x, y):
		dx = dout * 1 # remain as same vale: derivative of output 
		dy = dout * 1

		return dx, dy		

