'''
CNA Intern
Study name: gradient descent method(경사하강법)
Created by Eunseo Cho on 14/05/2017.
'''

import numpy as np
from id_soft import softmax_ftn
from error import cross_entropy_error
from gradient import numerical_gradient

class simpleNet:
	def __init__(self):
		self.W = np.random.randn(2,3)

	def predict(self, x):
		return np.dot(x, self.W)

	def loss(self, x, t):
		z = self.predict(x)
		y = softmax_ftn(z)
		loss = cross_entropy_error(y,t)

		return loss
def main():
	x = np.array([0.6, 0.9])
	t = np.array([0,0,1])

	net = simpleNet()

	f = lambda w: net.loss(x, t)
	dW = numerical_gradient(f, net.W)

	print("# 1 f")
	print(f)
	print("# 2 dW")
	print(dW)		

if __name__ == "__main__":
	main()	