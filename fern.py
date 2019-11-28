import numpy as np
import matplotlib.pyplot as plt
import random

class AffineTransform():
    """ Defines a general two dimensional affine transformation on the form A(x)+y.
        where A is the matrix given by (a,b) over (c,d), x is the input vector and
        y is a constant vector.

    """

    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0):
        """ initializes the class

            Parameters
            ----------

            a: The value of the upper left corner of the matrix.
            b: The value of the upper right corner of the matrix.
            c: The value of the bottom left corner of the matrix.
            d: The value of the bottom right corner of the matrix.
            e: The first value in the contant vector.
            f: The second value in the contant vector.

            Returns
            -------
            Nothing.

        """
        self.matrix = np.array([[a,b],[c,d]])
        self.constant = np.array([e,f])

    def __call__(self,x,y):
        """ Gives the result of the affine transformation for a specific
            input vector.

            Parameters
            ----------

            x: The x-coord of the input vector.
            y: The y-coord of the input vector.
            Returns
            -------
            The result of the affine transformation.

        """
        input = np.array([x,y])
        return np.matmul(self.matrix, input)+self.constant


""" Creates four instances of AffineTransform in order to generate the fern.
    The functions list contains the functions while fp_cumulative contains the
    corresponding cumulative probabilites needed to generate the fern

"""

f1 = AffineTransform(d = 0.16)
f2 = AffineTransform(0.85,0.04,-0.04,0.85,0,1.60)
f3 = AffineTransform(0.20,-0.26,0.23,0.22,0,1.60)
f4 = AffineTransform(-0.15,0.28,0.26,0.24,0,0.44)

functions = [f1, f2, f3, f4]
fp_cumulative = [0.01,0.86,0.93,1]

def next_point(x):
    """ Generates the next point of the fern.

        Parameters
        ----------

        x: two dimensional input vector.

        Returns
        -------
        The next point in the fern.

    """
    r = np.random.random()
    for j, p in enumerate(fp_cumulative):
        if r < p:
            return (functions[j](x[0],x[1]))

def fern_maker(n=100000):
    """ Function which generates the whole fern

        Parameters
        ----------

        n: The amount of points you want to generate.

        Returns
        -------
        All the points in the fern.

    """
    fern = np.zeros((n,2))
    for i in range(len(fern)-1):
        fern[i+1]=next_point(fern[i])
    return fern


if __name__=="__main__":
    #Genereates an example fern
    fern = fern_maker()
    plt.figure("Fern",figsize=(9, 9))
    plt.scatter(fern[:,0],fern[:,1], c="green", s=0.1)
    plt.axis('off')
    plt.savefig("fern.png")
    plt.show()
