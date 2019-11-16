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
        self._starting_point()


    def _generate_ngon(self):
        n = self.n
        self._corners = np.array([[np.sin(i*2*np.pi/(n)), np.cos(i*2*np.pi/(n))] for i in range(n)])

    def _starting_point(self):
        weight = np.random.random(self.n)
        weight = weight/np.sum(weight)      # normalizing the weights

        weighted_corners = np.array([self._corners[i] * weight[i] for i in range(self.n)])
        self.start_value = np.sum(weighted_corners, axis=0) # sum the linear combinations

    def plot_ngon(self):
        plt.scatter(*zip(*self._corners))
        plt.axis("equal")
        plt.axis("off")
       
    def plot_ngon_filled(self, X):
        plt.scatter(*zip(*X), s=0.2)#, marker=".")
        
        # Turn off *all* ticks & spines, not just the ones with colormaps.
        plt.axis("equal")
        #plt.axis("off")

    def iterate(self, steps, discard=5):
        r = self.r
        X = np.empty((steps, 2))       # matrix storing the points
        X[0] = self.start_value

        for i in range(steps-1):
            c = np.random.randint(self.n)
            X[i+1] = r * X[i] + (1-r) * self._corners[c]

        self.X = np.delete(X, (0, discard), axis=0)


    def plot(self, color=False, cmap_name="jet"):
        # Create figure and adjust figure height to number of colormaps

        if color == True:
            colors = self._corners
        else: 
            colors = "black"

        plt.scatter(*zip(*self.X), c=colors, cmap=cmap_name, s=0.2, marker=".")
        
        # Turn off *all* ticks & spines, not just the ones with colormaps.
        plt.axis("equal")
        plt.axis("off")

    def show(self, color=False, cmap_name="jet"):
        self.plot(color, cmap_name)
        plt.show()


if __name__ == "__main__":
    N = 100_000
    
    test = ChaosGame(3)
    # test.plot_ngon()
    test.iterate(N)
    test.show()
    #print(test.X)

   
    
    """
    for n in range(3, 9):
        test_plot_ngon = ChaosGame(n)
        plt.subplot(3,2,n-2)
        test_plot_ngon.plot_ngon()
        plt.title(f"{n}-gon")
    plt.subplots_adjust(hspace = 1)
    plt.show()
    ===============================


    test_pick_starting_point = ChaosGame(5)
    N = 10000  # number of staring points in test

    X = np.empty((N, 2))
    for i in range(N):
        test_pick_starting_point._starting_point()
        X[i] = test_pick_starting_point.start_value
        
    #plt.scatter(*zip(*X), s=1, marker=".")
    
    # Turn off *all* ticks & spines, not just the ones with colormaps.
    plt.axis("equal")
    #plt.axis("off")
    test_pick_starting_point.plot_ngon_filled(X)
    plt.show()
    """
   

