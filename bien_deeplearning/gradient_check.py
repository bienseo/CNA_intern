'''
CNA Intern
Study name: 오차역전파법(Backpropagation)으로 구한 기울기 검증하기
Created by Eunseo Cho on 22/05/2017.
'''

import sys, os
import numpy as np
from mnist import load_mnist
from TwoLayerNet import TwoLayerNet

# 데이터 읽기
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

x_batch = x_train[:3]
t_batch = t_train[:3]

grad_numerical = network.numerical_gradient(x_batch, t_batch)
grad_backprop = network.gradient(x_batch, t_batch)

print("Gradient check\n")
# 각 가중치의 절대 오차의 평균을 구한다.
for key in grad_numerical.keys():
	diff = np.average(np.abs(grad_backprop[key] - grad_numerical[key]))
	print(key + " : " + str(diff))