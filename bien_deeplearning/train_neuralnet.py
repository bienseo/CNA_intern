'''
CNA Intern
Date: 15/05/2017 - 22/05/2017
Study name: (Test) Train neural network: 오차역전파법을 사용한 학습 구현하기
Created by Eunseo Cho on 15/05/2017
'''
import sys, os
import numpy as np
import matplotlib.pyplot as plt
from mnist import load_mnist
from TwoLayerNet import TwoLayerNet


# 데이터 읽기
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

# hyperparameters
iters_num = 10000
train_size = x_train.shape[0]
batch_size = 100
learnig_rate = 0.1

train_loss_list = []
train_acc_list = []
test_acc_list = []

iter_per_epoch = max(train_size / batch_size, 1)

for i in range(iters_num):
	batch_mask = np.random.choice(train_size, batch_size)
	x_batch = x_train[batch_mask]
	t_batch = t_train[batch_mask]

	# 기울기 계산: 오차역전파법으로 기울기를 구한다.
	grad = network.gradient(x_batch, t_batch)

	# 갱신
	for key in ('W1', 'b1', 'W2', 'b2'):
		network.params[key] -= learnig_rate * grad[key]

	loss = network.loss(x_batch, t_batch)
	train_loss_list.append(loss)

	if i % iter_per_epoch == 0:
		train_acc = network.accuracy(x_train, t_train)
		test_acc = network.accuracy(x_test, t_test)
		train_acc_list.append(train_acc)
		test_acc_list.append(test_acc)
		print("train acc, test acc | " + str(train_acc) + ", " + str(test_acc))

# test
markers = {'train': 0, 'test': 's'}
x = np.arange(len(train_acc_list))
plt.plot(x, train_acc_list, label='train acc')
plt.plot(x, test_acc_list, label='test_acc', linestyle='--')
plt.xlabel("epochs")
plt.ylabel("accuracy")
plt.title("bienseo minibatch train")
plt.ylim(0, 1.0)
plt.legend(loc='lower right')	
plt.show()	