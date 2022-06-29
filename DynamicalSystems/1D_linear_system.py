import numpy as np
import pylab as plt

"""
Generate time-series of a 1D linear system
"""

T = 100
DX = np.zeros(T)
X  = np.zeros(T)

a = -0.01
x_0 = 10
X[0] = x_0

for t in range(1,T):
    DX[t] = a*X[t-1]
    X[t] = X[t-1] + DX[t]


colors = plt.cm.Spectral(np.linspace(0, 1, T-1))
plt.figure()
ax = plt.subplot(111)
ax.plot(X[:], c='black', lw=5)
ax.set_xticks(np.linspace(0, T, 4))
ax.set_xlim(0, T)
ax.set_xticklabels(np.round(np.linspace(0, T, 4), 0), fontsize=20)
ax.set_yticks(np.round(np.linspace(np.min(X), np.max(X), 4), 2))
ax.set_yticklabels(np.round(np.linspace(np.min(X), np.max(X), 4), 0), fontsize=20)
ax.set_xlabel(r'$T$', fontsize=20)
ax.set_ylabel(r'$x$', fontsize=20)
ax.spines['bottom'].set_linewidth(3)
ax.spines['left'].set_linewidth(3)
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
plt.tight_layout()
plt.show()


colors = plt.cm.Spectral(np.linspace(0, 1, T-1))
plt.figure()
ax = plt.subplot(111)
ax.scatter(X[1:], DX[1:], c=colors, s=10)
ax.set_xticks(np.linspace(np.min(X), np.max(X),   4))
ax.set_xticklabels(np.round(np.linspace(np.min(X), np.max(X), 4), 0), fontsize=20)
ax.set_yticks(np.round(np.linspace(np.min(DX), np.max(DX), 4), 2))
ax.set_yticklabels(np.round(np.linspace(np.min(DX), np.max(DX), 4), 0), fontsize=20)
ax.set_xlabel(r'$x$', fontsize=20)
ax.set_ylabel(r'$\dot{x}$', fontsize=20)
ax.spines['bottom'].set_linewidth(3)
ax.spines['left'].set_linewidth(3)
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
plt.tight_layout()
plt.show()