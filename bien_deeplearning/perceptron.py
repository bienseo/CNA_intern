'''
CNA Intern
Study name: perceptron 예제
Created by Eunseo Cho on 04/05/2017
'''

import numpy as np

def step_function(x):
    return 1 if x >= 0 else 0

def perceptron_output(weights, bias, x):
    calculation = np.dot(weights, x) + bias
    return step_function(calculation)

def main():
    x = [1, 0]
    weights = [2, 2]
    bias = - 3
    result = perceptron_output(weights, bias, x)
    print(result)

if __name__ == '__main__':
    main()    