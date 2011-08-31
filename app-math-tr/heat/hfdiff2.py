import numpy as np
import scipy.linalg

# Number of internal points
N = 200

# Calculate Spatial Step-Size
h = 1/(N+1.0)
k = h/2

x = np.linspace(0,1,N+2)
x = x[1:-1] # get rid of the '0' and '1' at each end

# Initial Conditions
u = np.transpose(np.mat(10*np.sin(np.pi*x)))

# second derivative matrix
I2 = -2*np.eye(N)
E = np.diag(np.ones((N-1)), k=1)
D2 = (I2 + E + E.T)/(h**2)

I = np.eye(N)
data = []

TFinal = 1
NumOfTimeSteps = int(TFinal/k)

for i in range(NumOfTimeSteps):
    # Solve the System: 
    # (I - k/2*D2) u_new = (I + k/2*D2)*u_old
    A = (I - k/2*D2)
    b = np.dot((I + k/2*D2), u)
    u = scipy.linalg.solve(A, b)
    data.append(u)

    
FPS = 20
MovieLength = 10
 
import matplotlib.pyplot as plt
import time

def plotFunction( frame ):
	plt.plot(x, data[int(NumOfTimeSteps*frame/(FPS*MovieLength))])
	plt.axis((0,1,0,10.1))
        
def CreateMovie(plotter, numberOfFrames, fps=10):
        plt.ion()
	for i in range(numberOfFrames):
		plotter(i) 
		plt.draw()
		time.sleep(0.2)
		plt.hold(False)
         
 
# Generate the movie
CreateMovie(plotFunction, int(MovieLength*FPS), FPS)

