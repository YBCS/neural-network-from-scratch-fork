# test.py

import mnist_loader
trainig_data, validation_data, test_data = mnist_loader.load_data_wrapper()
trainig_data = list(trainig_data)


import network

net = network.Network([784, 30, 10])
net.SGD(trainig_data, 30, 10,3.0, test_data = test_data)