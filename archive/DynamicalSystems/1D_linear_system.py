import numpy as np
import pylab as plt

import os
os.chdir('..')

"""
Generate time-series of a 1D linear system
"""

T = 100
I = 11
DX = np.zeros((T, I))
X  = np.zeros((T, I))

a = 0.05
x_0 = np.linspace(-10, 10, I)

for i in range(I):
    X[0, i] = x_0[i]
    for t in range(1,T):
        DX[t,i] = a*X[t-1,i]
        X[t,i] = X[t-1,i] + DX[t,i]


colors = plt.cm.Spectral(np.linspace(0, 1, I))
plt.figure(figsize=(4.8, 4.8))
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


colors = plt.cm.Spectral(np.linspace(0, 1, T-1))
plt.figure(figsize=(4.8, 4.8))
ax = plt.subplot(111)
ax.axvline(0.0, lw=3, color='black')
ax.axhline(0.0, lw=3, color='black')
ax.plot(x_0, np.sign(a)*x_0, color='black', lw=5)
for i in range(I):
    if a != 0:
        ax.arrow(x=x_0[i], y=0, dx=np.sign(a*x_0[i]), dy=0, head_width=0.2*x_0[i], head_length=1, color='black')
ax.set_xticks(np.linspace(np.min(X), np.max(X),   4))
ax.set_xticklabels(np.round(np.linspace(np.min(X), np.max(X), 4), 0), fontsize=20)
ax.set_yticks(np.round(np.linspace(np.min(DX), np.max(DX), 4), 2))
ax.set_yticklabels(np.round(np.linspace(np.min(DX), np.max(DX), 4), 0), fontsize=20)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(left=-10, right=10)
ax.set_ylim(bottom=np.min(x_0), top=np.max(x_0))
ax.set_xlabel(r'$x$', fontsize=20)
ax.set_ylabel(r'$\dot{x}$', fontsize=20)
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.left.set_visible(False)
ax.spines.bottom.set_visible(False)
plt.tight_layout()
plt.savefig('svg/1D_LS_a{}_PS.svg'.format(a))
plt.show()