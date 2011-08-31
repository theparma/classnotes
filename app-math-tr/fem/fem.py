import numpy as np

K = [[6., -3., 0],
     [-3., 6., -3.],
     [0., -3., 3.]
     ]

f = [1./3., 1./3., 1./6.]

print np.linalg.solve(K,f)

print 5./18., 4./9., 1./2.

