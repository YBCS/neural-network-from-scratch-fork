# test.py

import mnist_loader
trainig_data, validation_data, test_data = mnist_loader.load_data_wrapper()
trainig_data = list(trainig_data)


import network

net = network.Network([784, 30, 10])
# net.SGD(trainig_data, 30, 10, 3.0, test_data = test_data)
net.SGD(trainig_data, 3, 10, 3.0)





# plz define this and you work is done
# net.evalue_own(filename)
# while(True):
	#keep taking input and try different photos


## after the epocs try to use just one photo and get the output

# use jupyter to visualize all the shits