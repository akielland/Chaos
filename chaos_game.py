import numpy as np
import matplotlib.pyplot as plt
import os
import time

class ChaosGame:
    """ Calculating fractal distributions of points based on n-gons and
        returning them as color coded scatter plots.

        Parameters
        ----------
        n: int, size of n-gon (3 or above)
        r: float, ratio between previous point the corner decisive of next point
           default value: 0.5; range: (0, 1)

        Returns
        -------
        fig.png: the fractal figure
    """
    def __init__(self, n=3, r=0.5):
        self.n = n
        self.r = r

        if r < 0 or 1 < r:
            raise ValueError(f"r must be between 0 and 1; r is {r}")

        if n < 3:
            raise ValueError(f"n must be above at least 3; n is {n}")

        if not isinstance(n, int):
            raise TypeError(f"n must be of type integer; n is {type(n)}")

        self._generate_ngon()
        self._starting_point()


    def _generate_ngon(self):
        """ Generate array with the n-gon corner points."""
        n = self.n
        self._corners = np.array([[np.sin(i*2*np.pi/(n)), np.cos(i*2*np.pi/(n))] for i in range(n)])


    def _starting_point(self):
        """ Randomely select a start point."""
        weight = np.random.random(self.n)
        weight = weight/np.sum(weight)

        weighted_corners = np.array([self._corners[i] * weight[i] for i in range(self.n)])
        self.start_value = np.sum(weighted_corners, axis=0) # sum the linear combinations


    def iterate(self, steps, discard=5):
        """ Effectuate the fractal algorithm.

        Parameters
        ----------
        steps: int, number of iteration steps
        discard: int, the first iterative values that are to be deleted

        Attributes
        -------
        X: matrix, with generated fractal points
        _random_corners: array, store corners in iterative order
        """
        r = self.r
        X = np.empty((steps, 2))
        X[0] = self.start_value
        _random_corners = np.zeros(steps)

        for i in range(steps-1):
            c = np.random.randint(self.n)
            X[i+1] = r * X[i] + (1-r) * self._corners[c]
            _random_corners[i+1] = c

        self._random_corners = np.delete(_random_corners, (0, discard), axis=0)
        self.X = np.delete(X, (0, discard), axis=0)


    def _method_compute_color(self):
        """ Make a list of values for coding color based on color of previous point and corner vicinity """
        _color_value = []
        _color_value.append(self._random_corners[0])

        for i in range(len(self.X)-1):
            _color_value.append(0.5 * (_color_value[i] + self._random_corners[i+1]))

        return _color_value


    @property
    def color(self):
        return self._method_compute_color()


    def plot(self, color=False, cmap_name="jet"):
        """ Plot the fractal points.

        Arguments
        ---------
        color: Boolean, if True; color is determed by the list genrerated in
               the method _method_compute_color. If False; black is used
        cmap_name: matplotlib colormap
        The other parameters described in mehtod plot
        """
        if color:
            colors = self._method_compute_color()
        else:
            colors = "black"

        plt.scatter(*zip(*self.X), c=colors, cmap=cmap_name, s=0.2, marker=".")
        plt.axis("equal")
        plt.axis("off")


    def show(self, color=False, cmap_name="jet"):
        self.plot(color, cmap_name)
        plt.show()


    def savepng(self, outfile, color=False, cmap_name="jet"):
        """ Saves plot as png file only.

        Parameter
        ---------
        outfile: string, name of figure file
        The other parameters described in mehtod plot

        Raises
        ------
        NameError: If file name has extension other than .png
        """
        name, ext = os.path.splitext(outfile)

        if ext == ".png":
            filename = outfile
        elif not ext:
            filename = name + ".png"
        else:
            raise NameError ("Only accepted file extension is png")

        self.plot(color, cmap_name="jet")
        plt.savefig(filename, dpi=300, transparent=True)



if __name__ == "__main__":
    N = 100_000
    test = ChaosGame(6, 1/3)
    test.iterate(N)
    test.show(True)
   
