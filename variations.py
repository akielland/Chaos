import numpy as np
import matplotlib.pyplot as plt

class variations():
    """docstring for variations."""

    def __init__(self, xvals, yvals,colors="black"):
        self.x = xvals
        self.y = yvals
        self.colors = colors
        self.collection = {"linear":self.linear, "handkerchief":self.handkerchief, "swirl":self.swirl, "disc":self.disc, "fisheye":self.fisheye, "exponential":self.exponential}


    def __call__(self, coeff):
        u = np.zeros(self.x.shape)
        v = np.zeros(self.y.shape)
        for key in coeff:
            u_temp, v_temp = self.collection[key]()
            u = u+coeff[key]*u_temp
            v = v+coeff[key]*v_temp

        self.u = u
        self.v = v
        return u, v

    def linear(self):
        u = self.x
        v = self.y
        self.u = u
        self.v = v
        return u,v

    def handkerchief(self):
        r = np.sqrt(self.x**2+self.y**2)
        theta = np.arctan2(self.y,self.x)
        u = r*(np.sin(theta+r))
        v = r*np.cos(theta-r)
        self.u = u
        self.v = v
        return u,v

    def swirl(self):
        r2 = self.x**2+self.y**2
        u = self.x*np.sin(r2)-self.y*np.cos(r2)
        v = self.x*np.cos(r2)+self.y*np.sin(r2)
        self.u = u
        self.v = v
        return u,v

    def disc(self):
        r = np.sqrt(self.x**2+self.y**2)
        theta = np.arctan2(self.y,self.x)
        u = theta*np.sin(np.pi*r)/np.pi
        v = theta*np.cos(np.pi*r)/np.pi
        self.u = u
        self.v = v
        return u,v

    def fisheye(self):
        r = np.sqrt(self.x**2+self.y**2)
        u = 2*self.y/(r+1)
        v = 2*self.x/(r+1)
        self.u = u
        self.v = v
        return u,v

    def exponential(self):
        u = np.exp(self.x-1)*np.cos(np.pi*y)
        v = np.exp(self.x-1)*np.sin(np.pi*y)
        self.u = u
        self.v = v
        return u,v

    def plot(self,cmap):
        plt.scatter(self.u, -self.v, c=self.colors, cmap=cmap, s=0.1)
        plt.axis("equal")
        plt.axis("off")



x = np.linspace(-1,1,60)
y = np.linspace(-1,1,60)
xr , yr = np.meshgrid(x,y)
xf = xr.flatten()
yf = yr.flatten()
var = variations(xf,yf)
coeff = {"disc":0.5,"fisheye":0.5}
var(coeff)
var.plot("greys")
plt.show()
