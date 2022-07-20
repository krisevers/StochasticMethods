import numpy as np
import pylab as plt

import os
os.chdir('..')

def set_fig_params():
    ax = plt.subplot(111)
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    ax.spines['bottom'].set_linewidth(3)
    ax.spines['left'].set_linewidth(3)
    ax.tick_params(axis="x", direction="out", width=3, length=8)
    ax.tick_params(axis="y", direction="out", width=3, length=8)

def f(u, u_rest=0, u_rheo=10, d_T=1):
    '''
    Exponential Integrate-and-Fire
    '''
    return -(u - u_rest) + d_T * np.exp((u - u_rheo) / d_T)

u_rest  = 0
u_reset = 15
u_rheo  = 10
d_T     = 1.5
R = 1
I = 0

u = np.linspace(u_rest-1, u_reset, 100)
du = f(u, u_rest=u_rest, u_rheo=u_rheo, d_T=d_T) + R*I

plt.figure()
set_fig_params()
plt.plot(u, du, color='#c44343ff', lw=3)
plt.axvline(u_reset, ls='dotted', lw=3, c='black')
plt.axhline(0, ls='dashed', lw=3, c='black')
plt.xticks([u_rest, u_rheo, u_reset],
           [r'$u_{rest}$', r'$\vartheta_{rheo}$', r'$u_{reset}$'],
           fontsize=20)
plt.yticks([0], [0], fontsize=20)
plt.xlim(left=np.min(u), right=np.max(u)+1)
plt.ylim(bottom=-20, top=100)
plt.xlabel('u', fontsize=20)
plt.ylabel('du', fontsize=20)
plt.tight_layout()
plt.savefig('svg/EIF.svg')
plt.show()

# different input levels
num_exps = 6
d_T = 1.5
I = np.linspace(0, 20, num_exps)
u = np.linspace(u_rest-1, u_reset, 100)
du = np.empty(num_exps, dtype=object)
for e in range(num_exps):
    du[e] = f(u, u_rest=u_rest, u_rheo=u_rheo, d_T=d_T) + R*I[e]

colors = plt.cm.Greys_r(np.linspace(0, 1, num_exps))
plt.figure()
set_fig_params()
for e in range(num_exps):
    plt.plot(u, du[e], color=colors[e], lw=3, label=np.round(I[e], 2))
plt.axvline(u_reset, ls='dotted', lw=3, c='black')
plt.axhline(0, ls='dashed', lw=3, c='black')
plt.xticks([u_rest, u_rheo, u_reset],
           [r'$u_{rest}$', r'$\vartheta_{rheo}$', r'$u_{reset}$'],
           fontsize=20)
plt.yticks([0], [0], fontsize=20)
plt.xlim(left=np.min(u), right=np.max(u)+1)
plt.ylim(bottom=-20, top=100)
plt.legend(title=r'$I$', ncol=2, handlelength=0.5)
plt.xlabel('u', fontsize=20)
plt.ylabel('du', fontsize=20)
plt.tight_layout()
plt.savefig('svg/EIF_dI.svg')
plt.show()

# different d_T levels
num_exps = 11
I = 0
d_T = np.linspace(0, 2, num_exps)
d_T[0] = 0.1
u = np.linspace(u_rest-1, u_reset, 100)
du = np.empty(num_exps, dtype=object)
for e in range(num_exps):
    du[e] = f(u, u_rest=u_rest, u_rheo=u_rheo, d_T=d_T[e]) + R*I

colors = plt.cm.Spectral(np.linspace(0, 1, num_exps))
plt.figure()
set_fig_params()
for e in range(num_exps):
    plt.plot(u, du[e], color=colors[e], lw=3, label=np.round(d_T[e], 2))
plt.axvline(u_reset, ls='dotted', lw=3, c='black')
plt.axhline(0, ls='dashed', lw=3, c='black')
plt.xticks([u_rest, u_rheo, u_reset],
           [r'$u_{rest}$', r'$\vartheta_{rheo}$', r'$u_{reset}$'],
           fontsize=20)
plt.yticks([0], [0], fontsize=20)
plt.xlim(left=np.min(u), right=np.max(u)+1)
plt.ylim(bottom=-20, top=100)
plt.legend(title=r'$\Delta_T$', ncol=2, handlelength=0.5)
plt.xlabel('u', fontsize=20)
plt.ylabel('du', fontsize=20)
plt.tight_layout()
plt.savefig('svg/EIF_dT.svg')
plt.show()