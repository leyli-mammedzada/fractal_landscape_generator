import numpy as np
import random
import sys
from mayavi import mlab


# Create a 2D map and initialise the positions of its corners
def make_map(size, rand):
	mymap = np.zeros((size, size), dtype=float)
	mymap[0, 0] = random.uniform(-rand, rand)                # top left corner
	mymap[0, size - 1] = random.uniform(-rand, rand)         # top right corner
	mymap[size - 1, 0] = random.uniform(-rand, rand)         # bottom left corner
	mymap[size - 1, size - 1] = random.uniform(-rand, rand)  # bottom right corner
	return mymap


# The diamond step: set the midpoint by calculating the average of the corners and adding a random value
def diamond_step(themap, x, y, step, rand):
	north = themap[x, y - step]                 # find the north corner
	south = themap[x, y + step]                 # find the south corner
	east = themap[x + step, y]                  # find the east corner
	west = themap[x - step, y + step]           # find the west corner

	average = ((north + south + east + west) / 4)  # calculate the average
	themap[x, y] = average + rand  # set the midpoint by adding a random value to the average


# The square step: set the midpoint by calculating the average of the corners and adding a random value
def square_step(themap, x, y, step, rand):
	top_left = themap[x - step, y - step]       # find the top left corner
	top_right = themap[x + step, y - step]      # find the top right corner
	bottom_left = themap[x + step, y + step]    # find the bottom left corner
	bottom_right = themap[x - step, y + step]   # find the bottom right corner

	average = ((top_left + top_right + bottom_right + bottom_left) / 4)  # calculate the average
	themap[x, y] = average + rand  # set the midpoint by adding a random value to the average


# Loop through the map performing diamond and square steps until the half of the surface becomes too small
def diamond_square(themap, size, step, rand):
	x = size / 2
	y = size / 2
	middle = size / 2
	if (middle < 1):  # stop if surface too small
		return

	# perform diamond step
	for y in range(0, step, middle):
		for x in range((y + middle) % size, step, size):
			offset = random.uniform(-rand, rand)
			diamond_step(themap, x, y, middle, offset)

	# preform square step
	for y in range(middle, step, size): 
		for x in range(middle, step, size):
			offset = random.uniform(-rand, rand)
			square_step(themap, x, y, middle, offset)

	# recurse, reducing the size of the map and the range of the random value
	diamond_square(themap, size / 2, step, rand/1.4)
  

# Initialises values and calls the diamond_square function 
def main(size):
	size = 2 ** size + 1         # size of the map
	step = size - 1              # size of the itiration step (level)
	rand = 1                     # range of the random value
	themap = make_map(size,1)
	diamond_square(themap, size, step, rand)
	return themap


# The final landscape
Mymap = main(int(sys.argv[1]))


# Plotting
x, y = np.mgrid[-1:1:1j*int(sys.argv[1]),-1:1:1j*int(sys.argv[1])]
surf = mlab.surf(x, y, Mymap, colormap='gist_earth', warp_scale='auto')
mlab.show()
