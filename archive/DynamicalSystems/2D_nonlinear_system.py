import numpy as np
import pylab as plt

import os
os.chdir('..')

"""
Generate time-series of a 1D non-linear system (lotka-volterra)
"""

time = 100
dt = 1e-3
T = int(time/dt)
I = 10
DX = np.zeros((T, 2))
X  = np.zeros((T, 2, I))

alpha = 0.7
beta  = 0.5
gamma = 0.3
delta = 0.2
x_0 = np.array([1.0, 0.5])
x_0 = np.ones((I, 2))
x_0[:, 1] = np.linspace(0.1, 0.9, I)

for i in range(I):
    X[0, :, i] = x_0[i]
    for t in range(1,T):
        DX[t, 0] = X[t-1, 0, i] * (alpha - beta * X[t-1, 1, i]) * dt
        DX[t, 1] = X[t-1, 1, i] * (-gamma + delta * X[t-1, 0, i]) * dt
        X[t, :, i] = X[t-1, :, i] + DX[t]

plt.figure()
ax = plt.subplot(111)
ax.plot(X[:, 0, 0], c='grey',  lw=5)
ax.plot(X[:, 1, 0], c='black', lw=5)
ax.set_xticks(np.linspace(0, T, 4))
ax.set_xlim(0, T)
ax.set_xticklabels(np.round(np.linspace(0, T, 4), 0), fontsize=20)
ax.set_yticks(np.round(np.linspace(np.min(X), np.max(X), 4), 2))
ax.set_yticks([])
ax.set_xlabel(r'$T$', fontsize=20)
ax.set_ylabel(r'$x$', fontsize=20)
ax.spines['bottom'].set_linewidth(3)
ax.spines['left'].set_linewidth(3)
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
plt.tight_layout()
plt.savefig('svg/2D_NLS.svg')
plt.show()

plt.figure()
colors = plt.cm.Spectral(np.linspace(0, 1, I))
ax = plt.subplot(111)
for i in range(I):
    ax.plot(X[:, 0, i], X[:, 1, i], c=colors[i], lw=5)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel(r'$x$', fontsize=20)
ax.set_ylabel(r'$y$', fontsize=20)
ax.spines['bottom'].set_linewidth(3)
ax.spines['left'].set_linewidth(3)
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
plt.tight_layout()
plt.savefig('svg/2D_NS_PS.svg')
plt.show()