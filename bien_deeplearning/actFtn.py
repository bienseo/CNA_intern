'''
CNA Intern
Study name: Activation Function
Created by Eunseo Cho on 02/05/2017.
'''

import numpy as np
import matplotlib.pyplot as plt

def step_function(x):
    y = x > 0
    #  print(y)
    #  print(y.astype(np.int))
    return y.astype(np.int)

def sigmoid(x):
	h = 1 / (1 + np.exp(-x))
	return h

def sigmoid_grad(x):
    return (1.0 - sigmoid(x)) * sigmoid(x)

def relu(x):
	h = np.maximum(0, x)
	return h

def main():
    x1 = np.array([1, 2, 3])
    y1 = step_function(x1)
    
    x = np.arange(-5,5,0.5)
    y = step_function(x)
    f = np.arange(-5,5,0.5)
    g = sigmoid(f)
    fi = f
    fo = relu(fi)


    plt.plot(x,y,f,g,fi,fo)
    plt.show()


if __name__ == '__main__':
	main()