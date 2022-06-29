import numpy as np
import pylab as plt

import os
os.chdir('..')

"""
File to show the solution of a linear dynamical system.
"""

T = 100
I = 10
DX = np.zeros((T, I))
X  = np.zeros((T, I))

a = -0.05
x_0 = np.linspace(-10, 10, I)

for i in range(I):
    X[0, i] = x_0[i]
    for t in range(1,T):
        X[t,i] = X[0,i] * np.exp(a*t)


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
plt.savefig('svg/1D_LS_a{}.svg'.format(a))
plt.show()