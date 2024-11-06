import sys
sys.path.insert(0, '/home/mandara-hosur/Desktop/matgeo/codes/CoordGeo')
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

lib = ctypes.CDLL('./quescode.so')

check_lin = lib.checkLin
check_lin.restype = ctypes.c_int

if check_lin:
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    A=np.array(([-2,3,5])).reshape(-1,1)
    B=np.array(([1,2,3])).reshape(-1,1)
    C=np.array(([7,0,-1])).reshape(-1,1)

    x_BC = line_gen(B,C)
    x_AB = line_gen(A,B)

    ax.plot(x_BC[0,:],x_BC[1,:], x_BC[2,:],label='$BC$')
    ax.plot(x_AB[0,:],x_AB[1,:], x_AB[2,:],label='$AB$')


    colors = np.arange(1, 4)  # Example colors
    tri_coords = np.block([A, B, C])  # Stack A, B, C vertically
    ax.scatter(tri_coords[0, :], tri_coords[1, :], tri_coords[2, :], c=colors)
    vert_labels = ['A', 'B', 'C']

    for i, txt in enumerate(vert_labels):
        # Annotate each point with its label and coordinates
        ax.text(tri_coords[0, i], tri_coords[1, i], tri_coords[2, i], f'{txt}\n({tri_coords[0, i]:.0f}, {tri_coords[1, i]:.0f}, {tri_coords[2, i]:.0f})', fontsize=12, ha='center', va='bottom')

    ax.spines['top'].set_color('none')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')

    plt.grid() # minor
    plt.axis('equal')
    plt.savefig('fig.png')
