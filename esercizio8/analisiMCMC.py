import numpy as np
from scipy.optimize import minimize
from scipy import stats
import matplotlib.pyplot as plt
import emcee
import corner
import time
import pandas as pd

def flusso(p, E):
    m, b, alpha, mu, sigma=p
    return m*E+b+alpha* np.exp(-(E-mu)**2/(2*sigma**2))
def loglike_acc(p,E, f, ferr):
    return -0.5 * np.sum(((f- flusso(p, E))/ferr)**2)

def logprior(p):
    m, b, alpha, mu, sigma=p
    if( -1 < m < 1 and 9 < b < 11 and -6.5 < alpha < -4.5 and 3.75 < mu < 4.75 and -0.5 < sigma < 1.5):
        return 0.0
    return -np.inf

def logprob(p, E, f, ferr):
    lp = logprior(p)

    if np.isfinite(lp):
        return lp+loglike(p, E, f, ferr)
    return -np.inf

dati=pd.read_csv('absorption_line.csv')

E= dati['E'].values
f= dati['f'].values
ferr= dati['ferr'].values

plt.errorbar(E,f, yerr=ferr, color='pink')

gvng= np.array([ -0.2, 10, -5.5, 4.75, 0.5])
fgvng= flusso(gvng, E)

plt.errorbar( E, fgvng, color= 'crimson')
plt.show()

nw = 32

initial = gvng
ndim = len(initial)

p0 = np.array (initial) + 0.1*np.random.randn(nw, ndim)

sampler = emcee.EnsembleSampler( nw, ndim, logprob, args=(E, f, ferr))

print ("Running production ... ")
sampler.run_mcmc(p0, 2000, progress= True);

fig, axes = plt.subplots(ndim, figsize=(10, 9), sharex=True)
samples= sampler.get_chain()

labels = [r'$v_0 \;[m s^{-1}]$', r'$a [m s^{-2}]$' ]
for i in range(ndim):
    ax = axes[i]
    ax.plot(samples[:, :, i], "k", alpha=0.3)
    ax.set_xlim(0, len(samples))
    ax.set_ylabel(labels[i])
    ax.yaxis.set_label_coords(-0.1, 0.5)

axes[-1].set_xlabel("numero passi");

