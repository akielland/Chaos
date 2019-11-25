import numpy as np
import matplotlib.pyplot as plt
import random

class AffineTransform():
    """ Defines a general two dimensional affine transformation on the form A(x)+y.
    where A is the matrix given by (a,b) over (c,d), x is the input vector and
     y is a constant vector."""

    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0):
        self.matrix = np.array([[a,b],[c,d]])
        self.constant = np.array([e,f])

    def __call__(self,x,y):
        input = np.array([x,y])
        return np.matmul(self.matrix, input)+self.constant

""" The main program creates four instances of AffineTransform to create the fern.
The functions list contains the functions while fp_cumulative contains the
corresponding cumulative probabilites.

next_point calculates the next point in the
fern. It chooses a random function from functions based on the cumulative
probabilites.

fern_maker generates the whole fern by iterating next_point 100 000 times with an
initial point at origo. Returns an array containing x and y coords of every point
in the fern.

The last bit of code simply plots the fern with a green color.
"""

f1 = AffineTransform(d = 0.16)
f2 = AffineTransform(0.85,0.04,-0.04,0.85,0,1.60)
f3 = AffineTransform(0.20,-0.26,0.23,0.22,0,1.60)
f4 = AffineTransform(-0.15,0.28,0.26,0.24,0,0.44)

functions = [f1, f2, f3, f4]
fp_cumulative = [0.01,0.86,0.93,1]

def next_point(x):
    r = np.random.random()
    for j, p in enumerate(fp_cumulative):
        if r < p:
            return (functions[j](x[0],x[1]))

def fern_maker():
    fern = np.zeros((100_000,2))
    for i in range(len(fern)-1):
        fern[i+1]=next_point(fern[i])
    return fern


if __name__=="__main__":
    fern = fern_maker()
    plt.scatter(fern[:,0],fern[:,1], c="green", s=0.1)
    plt.savefig("fern.png")
    plt.show()
