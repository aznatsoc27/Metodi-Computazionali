import numpy as np
import sys, os

def somma (n):
    arr=np.arange(0,n+1,1)
    return arr.sum()

def sommarad (n):
    arr=np.arange(0,n+1,1)
    arrq=np.sqrt(arr)
    return arrq.sum()

