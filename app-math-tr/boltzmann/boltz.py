class Boltzmann:

    def __init__(self,n_iter=100,eta=0.1):
        self.n_iter = n_iter
        self.eta = eta
    
    def sigmoid(u):
        return 1./(1.+np.exp(-u));

    def draw(Sin,T):
        """
        draw - perform single Gibbs sweep to draw a sample from distribution
        """
        N=Sin.shape[0]
        S=Sin.copy()
        print S
        rand = np.random.rand(N,1)
        for i in xrange(N):
            h=np.dot(T[i,:],S)
            S[i]=rand[i]<sigmoid(h);

        return S

    def sample(T, n, num_init_samples):
        N=T.shape[0]
        print 'N',N
        s=np.random.rand(N)<sigmoid(0)
        for k in xrange(num_init_samples):
            s=draw(s,T)
        S=np.zeros((N,n))
        S[:,0]=s
        for i in xrange(1,n):
            S[:,i]=draw(S[:,i-1],T)
        return S

    def fit(self, X):
        R_data=np.dot(X,X.T)/A.shape[1];
        print R_data
        for i in range(self.n_iter):
            pass

        return A

import numpy as np

W = np.array([[0.2,0.3,0.5],
              [-0.2,0.1,-0.44],
              [0.2,-0.9,0.5]])
              
#res = sample(W,20,5)
#print res.shape
#print res

A = np.array([\
[0.,1.,1.,0],
[1.,1.,0, 0],
[1.,1.,1.,0],
[0, 1.,1.,1.],
[0, 0, 1.,0]
])

clf = Boltzmann()
print clf.fit(A)

