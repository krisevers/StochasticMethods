import numpy as np
import pylab as plt
from matplotlib.patches import Polygon

import os
os.chdir('..')

"""
Generate time-series of a 1D non-linear system (logistic equation)
"""

# T = 100
# I = 100
# DX = np.zeros((T, I))
# X  = np.zeros((T, I))
#
# a = -0.0
# x_0 = np.linspace(-10, 10, I)
#
# for i in range(I):
#     X[0, i] = x_0[i]
#     for t in range(1,T):
#         DX[t,i] = a*X[t-1,i] - X[t-1,i]**2
#         X[t,i] = X[t-1,i] + DX[t,i]

# colors = plt.cm.Spectral(np.linspace(0, 1, I))
# plt.figure(figsize=(4.8, 4.8))
# ax = plt.subplot(111)
# for i in range(I):
#     ax.plot(X[:,i], c=colors[i], lw=5)
# ax.set_xticks(np.linspace(0, T, 4))
# ax.set_xlim(0, T)
# ax.set_xticklabels(np.round(np.linspace(0, T, 4), 0), fontsize=20)
# ax.set_yticks(np.round(np.linspace(np.min(X), np.max(X), 4), 2))
# ax.set_yticks([])
# ax.set_xlabel(r'$T$', fontsize=20)
# ax.set_ylabel(r'$x$', fontsize=20)
# ax.spines['bottom'].set_linewidth(3)
# ax.spines['left'].set_linewidth(3)
# ax.spines.right.set_visible(False)
# ax.spines.top.set_visible(False)
# plt.tight_layout()
# plt.savefig('svg/1D_NLS_a{}.svg'.format(a))
# plt.show()

x = np.linspace(-5, 5, 100)
def f(x, a, b):
    return -(x-b)**a + 2

a = -2
b = -2

plt.figure(figsize=(4.8, 4.8))
ax = plt.subplot(111)
ax.axvline(0.0, lw=3, color='black')
ax.axhline(0.0, lw=3, color='black')
ax.plot(x, f(x, a=a, b=b), color='black', lw=5)
arr_x = np.linspace(-5, 5, 15)
for i in range(15):
    if a != 0:
        dir = np.sign(f(arr_x[i], a=a, b=b))
        length = 0.5
        width = 0.5
        top = [arr_x[i], width]
        bottom = [arr_x[i], -width]
        head = [arr_x[i]+dir*length, 0]
        pivot = Polygon(np.array([top, bottom, head]), facecolor='black')
        ax.add_patch(pivot)

if a != 0:
    x_0 = np.array([-2**(1/a) + b, 2**(1/a) + b])     # solutions for f(x) = 0
else:
    x_0 = []

for i in range(len(x_0)):
    if np.max(f(x, a=a, b=b)) >= 0:
        if np.sign(f(x_0[i]+0.0001, a=a, b=b)) > 0:
            plt.plot(x_0[i], 0, 'o', ms=14, markerfacecolor="white",
             markeredgecolor='black', markeredgewidth=5)
        else:
            plt.plot(x_0[i], 0, 'o', ms=14, markerfacecolor="black",
             markeredgecolor='black', markeredgewidth=5)

ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(left=-5, right=5)
ax.set_ylim(bottom=-10, top=10)
ax.set_xlabel(r'$x$', fontsize=20)
ax.set_ylabel(r'$\dot{x}$', fontsize=20)
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.left.set_visible(False)
ax.spines.bottom.set_visible(False)
plt.tight_layout()
plt.savefig('svg/1D_LS_a{}_PS.svg'.format(a))
plt.show()