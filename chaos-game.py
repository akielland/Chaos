import numpy as np 
import matplotlib.pyplot as plt 

class ChaosGame:
    """ Calculating fractal distributions of points based on n-gons and
        returning them as color coded scatter plots

        Parameters
        ----------
        n: size of n-gon (3 or above)
        r: ratio between previous point in a iterative manner to selected n-gon corner 
           default value: 0.5; range: (0, 1)


        Output
        ------
        fig.png

    """
    def __init__(self, n=3, r=0.5):
        self.n = n
        self.r = r

        # litt pussig error raise (2x)
        if r < 0 or 1 < r:
            raise ValueError(f"r must be between 0 and 1; r is {r}")

        if n < 3:
            raise ValueError(f"n must be above at least 3; n is {n}")

        if not isinstance(n, int):
            raise TypeError(f"n must be of type integer; n is {type(n)}")
        
        self._generate_ngon()
        #self._starting_point()


    def _generate_ngon(self):
        n = self.n
        self.c = np.array([[np.sin(i*2*np.pi/(n)), np.cos(i*2*np.pi/(n))] for i in range(n)])

    def _starting_point(self):
        w = np.random.random(self.n)
        w = w/np.sum(w)

        start = np.array([self.c[i] * w[i] for i in range(self.n)])
        starting_point = np.sum(start, axis=0)
        # print(starting_point)
        return starting_point

    def plot_ngon(self):
        plt.scatter(*zip(*self.c))

        plt.axis("equal")
        #plt.axis("off")
       
    def plot_ngon_filled(self, X):
        plt.scatter(*zip(*X), s=0.2)#, marker=".")

        plt.axis("equal")
        #plt.axis("off")

    def iterate(self, steps, discard=5):
        r = self.r
        self.X = np.empty((steps, 2))
        for i in range(steps-1):
            c = self._starting_point()
            self.X[i+1] = r * self.X[i] + (1-r) * c

        self.X = np.delete(self.X, (0, discard), axis=0)


if __name__ == "__main__":
    test = ChaosGame(5)
    test.iterate(10)
    

    """
    N = 1000
    X = np.empty((N, 2))
    for i in range(N):
        X[i] = test._starting_point()

    test.plot_ngon_filled(X)
    test.plot_ngon()
    plt.show()
    """

