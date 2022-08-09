import numpy as np
import pylab as plt
from matplotlib.patches import Rectangle

import os
os.chdir('..')

x = np.linspace(-5, 5, 100)

plt.figure(figsize=(4.8, 4.8))
ax = plt.subplot(111)
ax.axvline(0.0, lw=3, color='black')
ax.axhline(0.0, lw=3, color='black')
ax.plot(x, x**2, color='black', lw=5)
x_0 = 1
ax.plot(x, 2*x - x_0, color='#4872a1ff', lw=5)
ax.add_patch(Rectangle((x_0 - .5, 2*x_0 - x_0 - .5), 1, 1, facecolor="none", ec='k', ls='dotted', lw=5))

ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(left=-1, right=3)
ax.set_ylim(bottom=-2, top=5)
ax.set_xlabel(r'$x$', fontsize=20)
ax.set_ylabel(r'$y$', fontsize=20)
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.left.set_visible(False)
ax.spines.bottom.set_visible(False)
plt.tight_layout()
plt.savefig('svg/linearization.svg')
plt.show()