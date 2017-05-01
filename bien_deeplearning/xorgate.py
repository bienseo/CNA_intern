'''
CNA Intern
Study name: Logic gate
Created by Eunseo Cho on 01/05/2017.
'''
import numpy as np

def AND(x1, x2):
	x = np.array([x1, x2])
	w = np.array([0.5, 0.5])
	b = -0.75
	tmp = np.sum(w*x) + b
	if tmp <= 0:
		return 0
	else:
		return 1

def OR(x1, x2):
	x = np.array([x1, x2])
	w = np.array([0.5, 0.5])
	b = -0.25
	tmp = np.sum(w*x) + b
	if tmp <= 0:
		return 0
	else: 
		return 1

def NAND(x1, x2):
	x = np.array([x1, x2])
	w = np.array([-0.5, -0.5])
	b = 0.75
	tmp = np.sum(w*x) + b
	if tmp <= 0:
		return 0
	else: 
		return 1

'''
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y
'''

def XOR(x1, x2):
    notx1 = NAND(x1, x1)
    notx2 = NAND(x2, x2)
    s1 = AND(notx1, x2)
    s2 = AND(x1, notx2)
    y = OR(s1, s2)
    return y

def main():

	print("Logic gate\n\n")


	print("AND gate \n")
	for xi in [(0, 0), (0, 1), (1, 0), (1, 1)]:
		y = AND(xi[0], xi[1])
		print(str(xi) + " -> " + str(y))

	print("\n")

	print("OR gate \n")
	for xi in [(0, 0), (0, 1), (1, 0), (1, 1)]:
		y = OR(xi[0], xi[1])
		print(str(xi) + " -> " + str(y))

	print("\n")

	print("NAND gate \n")
	for xi in [(0, 0), (0, 1), (1, 0), (1, 1)]:
		y = NAND(xi[0], xi[1])
		print(str(xi) + " -> " + str(y))

	print("\n")

	print("XOR gate \n")
	for xi in [(0, 0), (0, 1), (1, 0), (1, 1)]:
		y = XOR(xi[0], xi[1])
		print(str(xi) + " -> " + str(y))

	print("\n")	


if __name__ == "__main__":
	main()    