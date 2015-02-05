# http://www.iro.umontreal.ca/~lisa/deep/data/mnist/mnist.pkl.gz
import cPickle, numpy as np, gzip, sys
from sklearn import neighbors
from sklearn.cross_validation import train_test_split
from smklearn.linear_model import LogisticRegression

np.random.seed(0)

import cPickle, numpy as np, gzip
f = gzip.open('/home/burak/Downloads/DeepLearningTutorials/data/mnist.pkl.gz', 'rb')
train_set, valid_set, test_set = cPickle.load(f)
f.close()
X_train,y_train = train_set
S = 1000
X_train = X_train[:S]
y_train = y_train[:S]
X_test,y_test = valid_set
X_test = X_test[:S]
y_test = y_test[:S]
print X_train.shape

# 85
# clf = neighbors.KNeighborsClassifier(n_neighbors=1)
# clf.fit(X_train, y_train)
# print 'KNN', clf.score(X_test, y_test)

# 78
# sys.path.append('../rbm')
# import rbms
# C = 1000
# r = rbms.BernoulliRBM(n_components=100,batch_size=100,n_iter=100)
# r.fit(X_train)
# clf = LogisticRegression(C=C)
# clf.fit(r.transform(X_train), y_train)
# res3 = clf.predict(r.transform(X_test))
# print 'RBM SK', np.sum(res3==y_test) / float(len(y_test))

# 75 num_hidden=100, learning_rate=0.2, max_epochs=100,num_visible=784,batch_size=50
# 79 num_hidden=150, learning_rate=0.1, max_epochs=100,num_visible=784,batch_size=80)
import rbmp
C = 1000
r = rbmp.RBM(num_hidden=150, learning_rate=0.1, max_epochs=100,num_visible=784,batch_size=80)
r.fit(X_train)
clf = LogisticRegression(C=C)
clf.fit(r.run_visible(X_train), y_train)
res3 = clf.predict(r.run_visible(X_test))
print 'RBM', np.sum(res3==y_test) / float(len(y_test))
