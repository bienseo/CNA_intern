'''
CNA Intern
Study name: numerical differentiation(수치미분)
Created by Eunseo Cho on 12/05/2017.
'''
import numpy as np
import matplotlib.pyplot as plt

def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)

def ftn1(x):
    return 0.01*x**2 + 0.1*x

def tangent_line(f, x):
    d = numerical_diff(f,x)
    y = f(x) - d*x
    return lambda t: d*t + y   

def main():
	x = np.arange(0.0, 20.0, 0.1)
	y = ftn1(x)
	point_diff = numerical_diff(ftn1, 5)
	print("x = 5 ->" + str(point_diff) + "\n")

	tf = tangent_line(ftn1, 5)
	y2 = tf(x)
	
	plt.plot(x,y)
	plt.xlabel("x")
	plt.ylabel("f(x)")

	plt.plot(x, y2)

	plt.show()

if __name__ == '__main__':
	main()



