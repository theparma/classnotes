class Boltzmann:

    def __init__(self,n_iter=100,eta=0.1,sample_size=100,init_sample_size=10):
        self.n_iter = n_iter
        self.eta = eta
        self.sample_size = sample_size
        self.init_sample_size = init_sample_size
    
    def sigmoid(self, u):
        return 1./(1.+np.exp(-u));

    def draw(self, Sin,T):
        """
        draw - perform single Gibbs sweep to draw a sample from distribution
        """
        N=Sin.shape[0]
        S=Sin.copy()
        print S
        rand = np.random.rand(N,1)
        for i in xrange(N):
            h=np.dot(T[i,:],S)
            S[i]=rand[i]<self.sigmoid(h);

        return S

    def sample(self, T):
        N=T.shape[0]
        s=np.random.rand(N)<self.sigmoid(0)
        for k in xrange(init_sample_size):
            s=self.draw(s,T)
        S=np.zeros((N,sample_size))
        S[:,0]=s
        for i in xrange(1,sample_size):
            S[:,i]=self.draw(S[:,i-1],T)
        return S

    def fit(self, X):
        R_data=np.dot(X,X.T)/A.shape[1];
        W_init = np.random.uniform(size=R_data.shape)
        W = W_init.copy()
        for i in range(self.n_iter):
            print 'Iteration', i
            

        return A

import numpy as np

W = np.array([[0.2,0.3,0.5],
              [-0.2,0.1,-0.44],
              [0.2,-0.9,0.5]])
              
clf = Boltzmann()
#clf.sample(W,20,5)
#exit()

A = np.array([\
[0.,1.,1.,0],
[1.,1.,0, 0],
[1.,1.,1.,0],
[0, 1.,1.,1.],
[0, 0, 1.,0]
])

print clf.fit(A)

