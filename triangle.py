import numpy as np 
import matplotlib.pyplot as plt 

corners = np.array([(0, 0), (1,0), (0.5, np.sqrt(0.75))])
plt.scatter(*zip(*corners))
#plt.show()

w = np.random.random(3)
w = w/np.sum(w)
start = np.array([corners[i] * w[i] for i in range(3)])
starting_point = np.sum(start, axis=0)

N = 10000
X = np.zeros((N,2))
X[0] = starting_point

######
colors = np.empty(N)
for i in range(N-1):
    corner = np.random.randint(0,3)
    X[i+1] = 0.5 * (X[i] + corners[corner])
    colors[i+1] = corner  

red = X[colors==0]
green = X[colors==1]
blue = X[colors==2]

plt.subplot(2,1,1)
plt.scatter(*zip(*red[5:-1]), s=0.1, marker=".", color="red")
plt.scatter(*zip(*green[5:-1]), s=0.1, marker=".", color="green")
plt.scatter(*zip(*blue[5:-1]), s=0.1, marker=".", color="blue")
plt.axis("equal")
plt.axis("off")

#####
colors = np.zeros((N,3))
corner_color = ((1,0,0), (0,1,0), (0,0,1))

for i in range(N-1):
    corner = np.random.randint(0,3)
    X[i+1] = 0.5 * (X[i] + corners[corner])
    colors[i+1] = 0.5 * (colors[i] + corner_color[corner])  

plt.subplot(2,1,2)
plt.scatter(*zip(*X), s=0.2, marker=".", c=colors)
plt.axis("equal")
plt.axis("off")

plt.savefig("trekanter.png")