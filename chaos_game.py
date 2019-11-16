import numpy as np 
import matplotlib.pyplot as plt 
import os

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



    def iterate(self, steps, discard=5):
        r = self.r
        X = np.empty((steps, 2))       # matrix storing the points
        X[0] = self.start_value
        _randome_corners = np.zeros(steps) 

        for i in range(steps-1):
            c = np.random.randint(self.n)
            X[i+1] = r * X[i] + (1-r) * self._corners[c]
            _randome_corners[i+1] = c

        self._randome_corners = np.delete(_randome_corners, (0, discard), axis=0)
        self.X = np.delete(X, (0, discard), axis=0)


    def _method_compute_color(self):
        _color_value = []
        _color_value.append(self._randome_corners[0])

        for i in range(len(self.X)-1):
            _color_value.append(0.5 * (_color_value[i] + self._randome_corners[i+1]))
        
        return _color_value


    def plot(self, color=False, cmap_name="jet"):
        # Create figure and adjust figure height to number of colormaps

        if color:
            colors = self._method_compute_color()
        else: 
            colors = "black"

        plt.scatter(*zip(*self.X), c=colors, cmap=cmap_name, s=0.2, marker=".")
        
        # Turn off *all* ticks & spines, not just the ones with colormaps.
        plt.axis("equal")
        plt.axis("off")


    def show(self, color=False, cmap_name="jet"):
        self.plot(color, cmap_name)
        plt.show()


    def savepng(self, outfile, color=False, cmap_name="jet"):
        name, ext = os.path.splitext(outfile)

        if ext == ".png":
            filename = outfile
        elif not ext:
            filename = name+".png"
        else:
            raise NameError ("Only accepted file extension is png")
        
        self.plot(color, cmap_name="jet")
        plt.savefig(filename, dpi=300, transparent=True)



if __name__ == "__main__":
    
# Creating figures:
    N = 100_000
    test_f = ChaosGame(6, 1/3)
    test_f.iterate(N)
    test_f.savepng("6-gon", True)
    




   

