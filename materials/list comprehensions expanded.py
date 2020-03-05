# test all the list composition of network.py
# for minor project

np.random.randn(x,y)	#return a list of random no btwn x,y wrt to standart variation of x and y ... 




arr = [1,2,3,4]
arr1 = [print(y,x) for x, y in zip(arr[:-1], arr[1:])]
print(arr1)


arr = [1,2,3,4]
# >>> arr[:-1]
# [1, 2, 3]
# >>> arr[1:]
# [2, 3, 4]
arr1 = [print(y,x) for x, y in zip(arr[:-1], arr[1:])]
# 2 1
# 3 2
# 4 3



# easy way to read python list composition
# read the for loop first ....

# np.argmax # Returns the indices of the maximum values along an axis
# returns the index of the max value in an array


#  the init function 

sizes = [768, 3, 1]
def theInitFunc(sizes):
	num_layers = len(sizes)
	biases = [np.random.randn(y, 1) for y in sizes[1:]]
	# print(sizes[:-1] + "\n" + sizes[1:])
	weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]

# there are 9 functions... we can do 1 a day maybe


# dat template -- python.. main... cmd input  

# expand 
training_inputs = [np.reshape(x, (784, 1)) for x in tr_d[0]]
[np.reshape(x, (784, 1)) for x in ["784 long array -- mnnist pic"]]