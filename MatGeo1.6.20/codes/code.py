#Code by GVV Sharma
#September 12, 2023
#Revised July 21, 2024
#released under GNU GPL
#Point Vectors


import sys                                          #for path to external scripts
sys.path.insert(0, '/home/shiny/matgeo/codes/CoordGeo')        #path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import Axes3D
import ctypes

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

# Load the shared object file
lib = ctypes.CDLL('./ccode.so')

# Define the function prototype
createMat = lib.createMat
createMat.restype = ctypes.POINTER(ctypes.c_int)
createMat.argtypes = [ctypes.c_int, ctypes.c_int]

# Call the function and initialize values to given points
A1 = createMat(-2,3,5)
B1 = createMat(1,2,3)
C1 = createMat(7,0,-1)

A = np.array(([A1[i] for i in range(3)])).reshape(-1,1)
B = np.array(([B1[i] for i in range(3)])).reshape(-1,1)
C = np.array(([C1[i] for i in range(3)])).reshape(-1,1)

# Create a figure and a 3D Axes
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

#Generating all lines
x_BC = line_gen(B,C)
x_AB = line_gen(A,B)

#Plotting all lines
ax.plot(x_BC[0,:],x_BC[1,:], x_BC[2,:],label='$BC$')

# Scatter plot
colors = np.arange(1, 4)  # Example colors
tri_coords = np.block([A, B, C])  # Stack A, B, C vertically
ax.scatter(tri_coords[0, :], tri_coords[1, :], tri_coords[2, :], c=colors)
vert_labels = ['A', 'B', 'C']

for i, txt in enumerate(vert_labels):
    # Annotate each point with its label and coordinates
    ax.text(tri_coords[0, i], tri_coords[1, i], tri_coords[2, i], f'{txt}\n({tri_coords[0, i]:.0f}, {tri_coords[1, i]:.0f}, {tri_coords[2, i]:.0f})',
             fontsize=12, ha='center', va='bottom')

ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

'''
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
'''
plt.grid() # minor
plt.axis('equal')

#if using termux
#plt.savefig('../figs/fig.png')
#subprocess.run(shlex.split("termux-open /sdcard/EE1030/MatGeo1.6.20/figs/fig.png"))
#else
#plt.show()
