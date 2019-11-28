import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import chaos_game as cg
import random
import os
from fern import fern_maker


class variations():
    """Class that transforms, plots and animates a set of coords according to
       inbulit methods.

    """

    def __init__(self, xvals, yvals, colors="black"):
        """ initializes the class with coordinates of points to be transformed
            along with point color.

            Parameters
            ----------
            xvals: Numpy array containing the x-coords of all points.
            yvals: Numpy array containing the y-coords of all points.
            colors: List containg color values for the points or simply a
                    string containing a color name compatible with matplotlib.

            Returns
            -------
            Nothing.

        """
        self.x = xvals
        self.y = yvals
        self.colors = colors
        self.dict = {}
        self.collection = {"linear":self.linear, "handkerchief":self.handkerchief,\
                            "swirl":self.swirl, "disc":self.disc,\
                            "fisheye":self.fisheye, "exponential":self.exponential}


    def __call__(self, coeff):
        """ Calling on the class returns transfomed x-coords and y-coords
            corresponding to the coeffecients in coeff

            Parameters
            ----------
            coeff: A dictionary where the keys are string containing method
                   names and corresponding coeffecients


            Returns
            -------
            Two arrays containing the transformed x-coords and y-coords respectively

        """
        u = np.zeros(self.x.shape)
        v = np.zeros(self.y.shape)
        coeff_sum = 0
        for key in coeff:
            u_temp, v_temp = self.collection[key]()
            u = u + coeff[key]*u_temp
            v = v + coeff[key]*v_temp
            coeff_sum = coeff_sum + coeff[key]
        assert (abs(coeff_sum-1)<(1/10000)), \
        "coeffecients in input dictionary must sum to 1"

        self.u = u
        self.v = v
        return u, v

    def linear(self):
        """ Method that simply returns the x and y coords as is and stores
            the result internally.

            Parameters
            ----------
            None.


            Returns
            -------
            Two arrays containing x-coords and y-coords respectively.

        """
        u = self.x
        v = self.y
        self.u = u
        self.v = v
        return u,v

    def handkerchief(self):
        """ Method that transforms the x and y coords according to the
            handkerchief equations, stores them internally and returns them.

            Parameters
            ----------
            None.


            Returns
            -------
            Two arrays containing the transformed x-coords and y-coords respectively.

        """
        r = np.sqrt(self.x**2 + self.y**2)
        theta = np.arctan2(self.x,self.y)
        u = r*(np.sin(theta + r))
        v = r*np.cos(theta - r)
        self.u = u
        self.v = v
        return u,v

    def swirl(self):
        """ Method that transforms the x and y coords according to the
            swirl equations, stores them internally and returns them.

            Parameters
            ----------
            None.


            Returns
            -------
            Two arrays containing the transformed x-coords and y-coords respectively.

        """
        r2 = self.x**2 + self.y**2
        u = self.x*np.sin(r2) - self.y*np.cos(r2)
        v = self.x*np.cos(r2) + self.y*np.sin(r2)
        self.u = u
        self.v = v
        return u,v

    def disc(self):
        """ Method that transforms the x and y coords according to the
            disc equations, stores them internally and returns them.

            Parameters
            ----------
            None.


            Returns
            -------
            Two arrays containing the transformed x-coords and y-coords respectively.

        """
        r = np.sqrt(self.x**2 + self.y**2)
        theta = np.arctan2(self.x,self.y)
        u = theta*np.sin(np.pi*r) / np.pi
        v = theta*np.cos(np.pi*r) / np.pi
        self.u = u
        self.v = v
        return u,v

    def fisheye(self):
        """ Method that transforms the x and y coords according to the
            fisheye equations, stores them internally and returns them.

            Parameters
            ----------
            None.


            Returns
            -------
            Two arrays containing the transformed x-coords and y-coords respectively.

        """
        r = np.sqrt(self.x**2 + self.y**2)
        u = 2*self.y / (r+1)
        v = 2*self.x / (r+1)
        self.u = u
        self.v = v
        return u,v

    def exponential(self):
        """ Method that transforms the x and y coords according to the
            exponential equations, stores them internally and returns them.

            Parameters
            ----------
            None.


            Returns
            -------
            Two arrays containing the transformed x-coords and y-coords respectively.

        """
        u = np.exp(self.x-1)*np.cos(np.pi*y)
        v = np.exp(self.x-1)*np.sin(np.pi*y)
        self.u = u
        self.v = v
        return u,v

    def plot(self, cmap="jet"):
        """ Method that plots the internally stored transformed x and y coords.

            Parameters
            ----------
            cmap: Is a cmap compatible with matplotlib.pyplot.scatter().


            Returns
            -------
            Nothing.

        """
        plt.scatter(self.u, -self.v, c=self.colors, cmap=cmap, s=0.1)
        plt.axis("equal")
        plt.axis("off")

    def savepng(self, outfile, cmap_name="jet"):
        """ Stores the transformed fractal as a png picture.

            Parameters
            ----------

            outfile: The outfiles filename
            cmap_name: Is a cmap compatible with matplotlib.pyplot.scatter().


            Returns
            -------
            Nothing.

        """
        name, ext = os.path.splitext(outfile)

        if ext == ".png":
            filename = outfile
        elif not ext:
            filename = name + ".png"
        else:
            raise NameError ("Only accepted file extension is png")

        self.plot(self, cmap_name="jet")
        plt.savefig(filename, dpi=300, transparent=True)

    def create_animation(self, dict_start, dict_end, t, cmap="jet"):
        """ Creates an animation from one variation to another at 60 fps.

            Parameters
            ----------

            dict_start: Dictionary containing the start values for the
                        variation coeffecients
            dict_end: Dictionary containing the end values for the
                      variation coeffecients


            Returns
            -------
            Nothing.

        """

        fig = plt.figure("Animation",figsize=(9, 9))
        plt.axes(xlim=(-1,1), ylim=(-1,1))
        plt.axis('off')
        self(dict_start)
        self.frame = plt.scatter(self.u, -self.v, c=self.colors, cmap=cmap, s=0.1)
        self.dictdata = {}
        self.keys = []
        for key in dict_start:
            self.keys.append(key)
            self.dictdata[key]=np.linspace(dict_start[key], dict_end[key], t*60)
        self.animation = animation.FuncAnimation(fig,
                                                 self._next_frame,
                                                 frames=range(t*60),
                                                 repeat=None,
                                                 interval=1/60,
                                                 blit=True)

    def _next_frame(self, i):
        """ Creates the next frame of the animation.

            Parameters
            ----------

            i: the method generates the ith frame of the animation


            Returns
            -------
            Nothing.

        """
        dict = {}
        for key in self.keys:
            values = self.dictdata[key]
            dict[key] = values[i]
        self(dict)
        points = np.array([self.u,-self.v]).transpose()
        self.frame.set_offsets(points)
        return self.frame,



    def save_animation(self, filename, fps=60):
        """ Saves the animation as an mp4.

            Parameters
            ----------

            filename: The name you want the file to have.
            fps: The fps you want to store the file as.


            Returns
            -------
            Nothing.

        """
        name, ext = os.path.splitext(filename)

        if ext == ".mp4":
            filename = filename
        elif not ext:
            filename = name + ".mp4"
        else:
            raise NameError ("Only accepted file extension is mp4")
        self.animation.save(filename, fps=fps)

def plot_grid():
    #Plots a simple grid for vizualisation purposes
    plt.plot([-1, 1, 1, -1, -1], [-1, -1, 1, 1, -1], color="grey")
    plt.plot([-1, 1], [0, 0], color="grey")
    plt.plot([0, 0], [-1, 1], color="grey")


if __name__=="__main__":

    varmethod = ["linear", "handkerchief", "swirl", "disc"]

    """ Makes a grid of points and plots them with the variations
        linear, disc, swirl and handkerchief.

    """
    x = np.linspace(-1,1,60)
    y = np.linspace(-1,1,60)
    xr , yr = np.meshgrid(x,y)
    xf = xr.flatten()
    yf = yr.flatten()
    grid = variations(xf,yf)
    plt.figure("grid",figsize=(9, 9))
    for i in range(4):
        plt.subplot(2,2,i+1)
        plot_grid()
        var = varmethod[i]
        grid.collection[var]()
        grid.plot()
        plt.title(var)



    """ Makes a square-fractal and plots it with the variations
        linear, disc, swirl and handkerchief.

    """
    square = cg.ChaosGame(4,1/3)
    square.iterate(10000)
    x = square.X[:,0]
    y = square.X[:,1]
    color = square.color
    squares = variations(x,-y,color)
    plt.figure("4-gon",figsize=(9, 9))
    for i in range(4):
        plt.subplot(2,2,i+1)
        var = varmethod[i]
        squares.collection[var]()
        squares.plot()
        plt.title(var)
    plt.savefig("4-gons.png")

    """ Makes a Barnley-fern and plots it with the variations
        linear, disc, swirl and handkerchief.

    """
    fern = fern_maker()
    x = fern[:,0]
    y = fern[:,1]
    max = (np.sqrt(x**2+y**2)).max()
    x = x/max
    y = y/max
    ferns = variations(x,-y,"green")
    plt.figure("Ferns",figsize=(9, 9))
    for i in range(4):
        plt.subplot(2,2,i+1)
        var = varmethod[i]
        ferns.collection[var]()
        ferns.plot()
        plt.title(var)
    plt.savefig("Ferns.png")

    """ Plots the barnely-fern with four different random combinations of
        linear and swirl chosen randomly from a uniform distribution.

    """
    plt.figure("FernSwirl",figsize=(9, 9))
    for i in range(4):
        plt.subplot(2,2,i+1)
        w = random.random()
        dict = {"linear":1-w,"swirl":w}
        ferns(dict)
        ferns.plot()
        plt.title("swirl = {}".format(w))
    plt.savefig("Fernswirl.png")

    """ Plots a hexagon-fractal and animates it with coeffecients from the
        start dictionary to the picture with the end dictionary over a period of 10
        seconds and saves the file.

    """
    sixgon = cg.ChaosGame(6,1/3)
    sixgon.iterate(10000)
    x = sixgon.X[:,0]
    y = sixgon.X[:,1]
    color = sixgon.color
    sixgons = variations(x,-y,color)
    dict_start = {"linear":1, "disc":0, "handkerchief":0, "exponential":0}
    dict_end = {"linear":0, "disc":0.5, "handkerchief":0.1, "exponential":0.4}
    sixgons.create_animation(dict_start, dict_end, 10)
    sixgons.save_animation("6-gon_animation.mp4",60)

    plt.show()
