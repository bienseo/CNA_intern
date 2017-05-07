'''
CNA Intern
Study name: mean squared error(MSE), cross entropy error(CEE)
Created by Eunseo Cho on 08/05/2017.
'''

import numpy as np

def mean_squared_error(y, t):
	e = 0.5 * np.sum((y - t) **2)

	return e

def cross_entropy_error(y, t):
	delta = 1e-7
	e = -np.sum(t * np.log(y + delta))

	return e
