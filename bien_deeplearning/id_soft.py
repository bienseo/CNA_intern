'''
CNA Intern
Study name: identity function for regression & softmax function for classification 
Created by Eunseo Cho on 06/05/2017.
'''
# jupyter qtconsole -> from id_soft import *

import numpy as np

def identity_ftn(a):
	y = a

	return y
'''
def softmax_ftn(a):
	c = np.max(a)
	exp_a = np.exp(a - c) # prevent overflow
	sum_exp_a = np.sum(exp_a)
	y = exp_a / sum_exp_a

	return y
'''
def softmax_ftn(x):
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T 

    x = x - np.max(x) # 오버플로 대책
    return np.exp(x) / np.sum(np.exp(x))	