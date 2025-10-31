import numpy as np
import pylab as plt

np.random.seed(1)

plt.figure()

T = 1
N = 500
dt = T/N 

# Brownian path simulation
plt.subplot(2, 1, 1)
plt.title('Brownian path simulation')

dW = np.zeros(N)
W  = np.zeros(N)

dW[0] = np.sqrt(dt)*np.random.randn()
W[0]  = dW[0]

for j in range(1, N):
	dW[j] = np.sqrt(dt)*np.random.randn()
	W[j]  = W[j-1] + dW[j]

plt.plot(np.arange(0, T, dt), W)
plt.xlabel('t')
plt.ylabel('W')




# Brownian path vectorized
plt.subplot(2, 1, 2)
plt.title('Brownian path vectorized')

dW = np.sqrt(dt)*np.random.randn(N)
W  = np.cumsum(dW)

plt.plot(np.arange(0, T, dt), W)
plt.xlabel('t')
plt.ylabel('W')


plt.tight_layout()
plt.show()