import numpy as np 
import matplotlib.pyplot as plt

""" Calculating a specific fractal distributions of points within a 3-gon 
    in an iterative manner.

    Algorithm:
    1. First randomely selection of one the corner points.
    2. New point is localized half way between the selected corner point
       and previous point.

    Returns
    -------
    Two scatter plots in a png file:
        1. Color coded with red, green and blue
        2. Color coded with RGB color based on iterative corner
""" 
#: array of corner points
corners = np.array([(0, 0), (1,0), (0.5, np.sqrt(0.75))])
plt.subplot(2,2,1)
plt.scatter(*zip(*corners),  marker="x", color="black")

#: array with a randomely selected start point (also test ploted)
starting_point = np.empty((1000,2))
for n in range(1000):
    w = np.random.random(3)
    w = w/np.sum(w)
    start = np.array([corners[i] * w[i] for i in range(3)])
    starting_point[n] = np.sum(start, axis=0)

plt.subplot(2,2,2)
plt.scatter(*zip(*starting_point), s=0.3, color="black")

#: matrix to store iterated points
N = 10000
X = np.zeros((N,2))
X[0] = starting_point[0]

#: plot with iterated points in three colors chosen based corner vicinities
colors = np.empty(N)
for i in range(N-1):
    corner = np.random.randint(0,3)
    X[i+1] = 0.5 * (X[i] + corners[corner])
    colors[i+1] = corner

X_reduced = np.delete(X, np.s_[0:5], axis=0)
colors_reduced = np.delete(colors, np.s_[0:5])

red = X_reduced[colors_reduced==0]
green = X_reduced[colors_reduced==1]
blue = X_reduced[colors_reduced==2]

plt.subplot(2,2,3)
plt.scatter(*zip(*red), s=0.1, marker=".", color="red")
plt.scatter(*zip(*green), s=0.1, marker=".", color="green")
plt.scatter(*zip(*blue), s=0.1, marker=".", color="blue")
plt.axis("equal")
plt.axis("off")

#: ploting iterated points RGB colore coded based on color of previous point and corner vicinity 
colors = np.zeros((N,3))
corner_color = ((1,0,0), (0,1,0), (0,0,1))

for i in range(N-1):
    corner = np.random.randint(0,3)
    X[i+1] = 0.5 * (X[i] + corners[corner])
    colors[i+1] = 0.5 * (colors[i] + corner_color[corner])  

plt.subplot(2,2,4)
plt.scatter(*zip(*X), s=0.2, marker=".", c=colors)
plt.axis("equal")
plt.axis("off")

plt.savefig("trekanter.png")