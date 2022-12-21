import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy

mypluto= pd.read_csv('vel_vs_time.csv')

plt.plot(mypluto['t'], mypluto['v'])
plt.show()
