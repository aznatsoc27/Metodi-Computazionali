import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import es1reco as rc

def imm(mod,sens,time):
    j=len(mod)
    ril=np.empty(0)
    ril=np.append(ril,[rc.Hit(mod[i], sens[i], time[i]) for i in range (j)])
    return ril

data0= pd.read_csv('hit_times_M0.csv')
data1= pd.read_csv('hit_times_M1.csv')
data2= pd.read_csv('hit_times_M2.csv')
data3= pd.read_csv('hit_times_M3.csv')

print(data0)

plt.hist(data0['hit_time'], bins=65)
plt.show()

deltaT= np.diff(data0['hit_time'].values)
mask= deltaT>0
logdelta=np.log10(deltaT[mask])

plt.hist(logdelta, bins=65, color='orange')
plt.show()

a=imm(data0['mod_id'].values, data0['det_id'].values, data0['hit_time'].values)
b=imm(data1['mod_id'].values, data1['det_id'].values, data1['hit_time'].values)
c=imm(data2['mod_id'].values, data2['det_id'].values, data2['hit_time'].values)
d=imm(data3['mod_id'].values, data3['det_id'].values, data3['hit_time'].values)

tot=np.append(a,b)
tot=np.append(tot,c)
tot=np.append(tot,d)

tot=np.sort(tot)

deltaT1= np.diff(tot).astype(np.float64)
mask1 = deltaT1>0
logdelta1=np.log10(deltaT1[mask1])

plt.hist(logdelta1, bins=65, color='red')
plt.show()

def insieme_eventi(array_hit):
    ie=np.empty(0)
    deltat=np.logspace(1,1000000,65)
    
