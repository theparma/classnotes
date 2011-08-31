import numpy as np
import scipy
from matplotlib import pyplot as plt

tempdata = np.loadtxt("sunspots.dat")

year=tempdata[:,0]

Y=tempdata[:,1]

N = len(Y)

w = np.exp((2*np.pi*1j)/N)

W = np.zeros((N,N), complex)
for i in range(N):
    for k in range(N):
        W[i,k] = w**(i*k)
        
C = np.dot(np.linalg.inv(W), Y) 

C[30:-30] = 0.

Y_new = scipy.real(np.dot(W, C)) 

plt.plot(year, Y, 'g')
plt.hold(True)
plt.plot(year, Y_new, 'r')

plt.show()


