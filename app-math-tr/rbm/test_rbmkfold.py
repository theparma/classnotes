import cPickle, numpy as np, rbm
from sklearn.linear_model import LogisticRegression

from sklearn.base import BaseEstimator
from sklearn.base import TransformerMixin

class SKRBM(BaseEstimator, TransformerMixin):
    """
    Bu sinif bizim RBM kodu ile sklearn arasinda baglantiyi kurmak
    icin yazildi, tek yaptigi parametreleri alip RBM'i cagirmak, bu
    baglanti aslinda KFold icin muhakkak lazim degil (run_visible ile
    de bu isi halledebilirdik), fakat GridSearch kullanmak gerekirse
    class'in icinde transform() cagrisinin olmasi lazim.
    """
    def __init__(self, n_components=-1, learning_rate=-1, n_iter=-1,num_visible=-1):
      self.n_components = n_components
      self.learning_rate = learning_rate
      self.n_iter = n_iter
      self.num_visible = num_visible
      self.rbm_ = rbm.RBM(num_hidden=self.n_components,
                          learning_rate=self.learning_rate,
                          max_epochs=self.n_iter,num_visible=num_visible)

    def transform(self, X):
      return self.rbm_.run_visible(X)

    def fit(self, X, y=None):
      self.rbm_.fit(X)
      return self

X = np.loadtxt('../../stat/stat_mixbern/binarydigits.txt')
Y = np.ravel(np.loadtxt('../../stat/stat_mixbern/bindigitlabels.txt'))

np.random.seed(0)

from sklearn.cross_validation import KFold
scores = []
cv = KFold(n=len(X),n_folds=3)
for train, test in cv:
    X_train, Y_train = X[train], Y[train]
    X_test, Y_test = X[test], Y[test]
    r = SKRBM(n_components=40, learning_rate=0.3, n_iter=500,num_visible=64)
    r.fit(X_train)
    clf = LogisticRegression(C=1000)
    clf.fit(r.transform(X_train), Y_train)
    res3 = clf.predict(r.transform(X_test))
    scores.append(np.sum(res3==Y_test) / float(len(Y_test)))        
    
print np.mean(scores)
