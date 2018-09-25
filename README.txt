Implementation
My implementation of a fractal landscape generator follows the Diamond-Square algorithm.
1. The program uses the size n entered by the user.
2. Set the range of the random value to be (-1, 1).
2. The program creates a square surface of size 2*n+1 and initializes the positions of its corners using random values.
3. The program loops through the map and performs diamond and square steps on each iteration:
   • Diamond step: set the midpoint of each square by calculating the average of the corners and adding a random value.
   • Square step:  set the midpoint of each diamond by calculating the average of the corners and adding a random value.
4. The program recurses, decreasing the size of the map and the range of the random value.
5. Return the modified map.
6. Plot the heightmap in 3D


Compilation
To compile the program mlab package mayavi is needed (for plotting)
To compile the Diamond_Square.py program, use the command 
python2 Diamond_Square.py  <size>


3.4 Future Improvements
There is still a lot to improve in my implementation of the Diamond-Square algorithm. I am hoping to achieve more realistic results with smoother edges and for larger scales.
Also, there is a possibility of adding detail on landscapes (water bodies, trees, etc.).
