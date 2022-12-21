import sys
import numpy as np
import scipy 
import matplotlib.pyplot as plt

def random_walk (step, n):
    x=np.array([0])
    y=np.array([0])
    unif=np.random.uniform(low=0, high=2*np.pi, size=n)
    x1=0
    y1=0
    for i in unif:
        x1=x1+step*np.cos(i)
        x=np.append(x, x1)
        y1=y1+step*np.sin(i)
        y=np.append(y,y1)
    return x,y

passo=1
numpassi=1000
for j in range(6):
    fun = random_walk(passo, numpassi)
    plt.plot(fun[0], fun[1])

passo10x=np.zeros[10]
passo10y=np.zeros[10]
passo100x=np.zeros[100]
passo100y=np.zeros[100]
passo1000x=np.zeros[1000]
passo1000y=np.zeros[1000]

for i in range(1000):
    x,y= random_walk (1, 1000)
    passo10x[i]= passo10x[10]
    passo10y[i]= passo10y[10]
    passo100x[i]=passo100x[100]
    passo100y[i]=passo100y[100]
    passo1000y[i]=passo1000y[1000]
    passo1000x[i]=passo1000x[1000]


plt.xlabel('x')
plt.ylabel('y')
plt.show()

