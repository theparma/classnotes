import cPickle, numpy as np, gzip, rbm4
from sklearn import neighbors
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression

X = np.loadtxt('binarydigits.txt')
Y = np.ravel(np.loadtxt('bindigitlabels.txt'))

from sklearn.cross_validation import KFold
scores = []
cv = KFold(n=len(X),n_folds=3)
for train, test in cv:
    X_train, Y_train = X[train], Y[train]
    X_test, Y_test = X[test], Y[test]
    r = rbm4.SKRBM(n_components=30, learning_rate=0.3, n_iter=300)
    r.fit(X_train)
    clf = LogisticRegression(C=100)
    clf.fit(r.transform(X_train), Y_train)
    res3 = clf.predict(r.transform(X_test))
    scores.append(np.sum(res3==Y_test) / float(len(Y_test)))        
    
print np.mean(scores)
            
# 98    
    
