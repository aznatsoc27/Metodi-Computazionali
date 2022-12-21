import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import constants, fft


data1= pd.read_csv('data_sample1.csv')
data2= pd.read_csv('data_sample2.csv')
data3= pd.read_csv('data_sample3.csv')

t1= np.array(data1 ['time'])
t2= np.array(data2 ['time'])
t3= np.array(data3 ['time'])

a1= np.array(data1 ['meas'])
a2= np.array(data2 ['meas'])
a3= np.array(data3 ['meas'])

plt.plot(t1, a1, color= 'grey')
plt.plot(t2, a2, color= 'magenta')
plt.plot(t3, a3, color= 'red')

plt.xlabel('t')
plt.ylabel('f')

plt.show()

fft1= fft.fft(a1)
fft2= fft.fft(a2)
fft3= fft.fft(a3)

a=0.5

freq1= a*fft.fftfreq(fft1.size, d=1)
freq2= a*fft.fftfreq(fft2.size, d=1)
freq3= a*fft.fftfreq(fft3.size, d=1)

plt.plot((np.absolute(freq1[:freq1.size//2]))**2, (np.absolute(fft1[:fft1.size//2]))**2, 'o', markersize=4, color='grey')
plt.plot((np.absolute(freq2[:freq2.size//2]))**2, (np.absolute(fft2[:fft2.size//2]))**2, 'o', markersize=4, color= 'magenta')
plt.plot((np.absolute(freq3[:freq3.size//2]))**2, (np.absolute(fft3[:fft3.size//2]))**2, 'o', markersize=4, color= 'red')

plt.xscale('log')
plt.yscale('log')

plt.show()


