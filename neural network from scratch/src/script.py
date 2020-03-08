# This script attempts to do just this
'''
greyscaled, nparray, thumbnair (resize 28x28)
-------------------------------------------------------------------------------
this may not work as my photo is not clean enough 
either 
	improve input quality (clear white bg pixel value should be zero) 
	or change input technique (maybe drawn with mouse in a window pop up)
'''

import sys
from PIL import Image
import numpy as np

def load_image(filename):
	# this is normal laoding in PIL
	img = Image.open("../data/" + filename)
	# convert image to greyscale
	gs_img = img.convert(mode = 'L')
	# resize to 28 x 28
	gs_img = gs_img.resize((28, 28))
	# convert image to numpy array
	data = np.asarray(gs_img)

	data_input = [y for x in data for y in x]
	data_input = np.array(data_input)

	data_input = np.reshape(data_input, (784, 1))

	print(data_input.shape)
	# print(type(data_input))
	print(data_input)



def main():
	# cmd args are String 
	load_image(sys.argv[1])

	# change this to input an image each time	
	n = int(input("enter a num "))
	while n:
		try:
			print("you entered " + str(n-1) + (" plus one"))
			n = int(input("enter a num "))
		except ValueError:
			break;



if __name__ == '__main__':
	main()





