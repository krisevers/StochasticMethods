import numpy as np
import pylab as plt

import os
os.chdir('..')

"""
Generate time-series of a 1D non-linear system (logistic equation)
"""

T = 100
I = 10
DX = np.zeros((T, I))
X  = np.zeros((T, I))

a = -0.001
x_0 = np.linspace(-0.001, 0.001, I)

for i in range(I):
    X[0, i] = x_0[i]
    for t in range(1,T):
        DX[t,i] = a*X[t-1,i] - X[t-1,i]**2
        X[t,i] = X[t-1,i] + DX[t,i]

colors = plt.cm.Spectral(np.linspace(0, 1, I))
plt.figure()
ax = plt.subplot(111)
for i in range(I):
    ax.plot(X[:,i], c=colors[i], lw=5)
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
plt.savefig('svg/1D_NLS_a{}.svg'.format(a))
plt.show()


colors = plt.cm.Spectral(np.linspace(0, 1, T-1))
plt.figure()
ax = plt.subplot(111)
for i in range(I):
    ax.plot(X[1:,i], DX[1:,i], color='black', lw=5)
ax.set_xticks(np.linspace(np.min(X), np.max(X),   4))
ax.set_xticklabels(np.round(np.linspace(np.min(X), np.max(X), 4), 0), fontsize=20)
ax.set_yticks(np.round(np.linspace(np.min(DX), np.max(DX), 4), 2))
ax.set_yticklabels(np.round(np.linspace(np.min(DX), np.max(DX), 4), 0), fontsize=20)
ax.set_xticks([])
ax.set_yticks([])
ax.axvline(0.0, lw=3, color='black')
ax.axhline(0.0, lw=3, color='black')
ax.set_xlabel(r'$x$', fontsize=20)
ax.set_ylabel(r'$\dot{x}$', fontsize=20)
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.left.set_visible(False)
ax.spines.bottom.set_visible(False)
plt.tight_layout()
plt.savefig('svg/1D_NLS_a{}_PS.svg'.format(a))
plt.show()