import cPickle, numpy as np, rbmp, sys
from sklearn.linear_model import LogisticRegression

from sklearn.base import BaseEstimator
from sklearn.base import TransformerMixin

X = np.loadtxt('../../stat/stat_mixbern/binarydigits.txt')
Y = np.ravel(np.loadtxt('../../stat/stat_mixbern/bindigitlabels.txt'))

np.random.seed(0)

from sklearn.cross_validation import KFold

sys.path.append('../rbm')
import rbms
scores = []
cv = KFold(n=len(X),n_folds=3)
for train, test in cv:
    X_train, Y_train = X[train], Y[train]
    X_test, Y_test = X[test], Y[test]
    r = rbms.BernoulliRBM(n_components=40,batch_size=10,learning_rate=0.1,n_iter=100)
    r.fit(X_train)
    clf = LogisticRegression(C=1000)
    clf.fit(r.transform(X_train), Y_train)
    res3 = clf.predict(r.transform(X_test))
    scores.append(np.sum(res3==Y_test) / float(len(Y_test)))            
print np.mean(scores)
exit()

scores = []
cv = KFold(n=len(X),n_folds=3)
for train, test in cv:
    X_train, Y_train = X[train], Y[train]
    X_test, Y_test = X[test], Y[test]
    #learning_rate=0.1, max_epochs=100,num_visible=64,batch_size=10) 99
    r = rbmp.RBM(num_hidden=40, learning_rate=0.1, max_epochs=100,num_visible=64,batch_size=10)
    r.fit(X_train)
    clf = LogisticRegression(C=1000)
    clf.fit(r.run_visible(X_train), Y_train)
    res3 = clf.predict(r.run_visible(X_test))
    scores.append(np.sum(res3==Y_test) / float(len(Y_test)))        
    
print np.mean(scores)
