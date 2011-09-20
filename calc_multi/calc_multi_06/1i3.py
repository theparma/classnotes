from pylab import *
import time

plt.ion()

xmax = 10.
xmin = -10.
D = 20
x = linspace(xmin, xmax, D)
xlim(-10,10)
ylim(-10,10)

for t in linspace(-3., 3., 30):
    plot (x,((2. - x)/2.))
    plt.hold(True)
    quiver(0,0,2*cos(t)**2,sin(t)**2)
    plt.hold(True)
    plot(2*cos(t)**2,sin(t)**2,'rd')
    plt.hold(True)
    plt.draw()
    time.sleep(1)
    plt.hold(False)

