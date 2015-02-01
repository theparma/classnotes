from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import BernoulliRBM
from sklearn.grid_search import GridSearchCV
from sklearn.pipeline import Pipeline
import numpy as np
import argparse, rbms
import time

x = np.loadtxt('binarydigits.txt')
labels = np.ravel(np.loadtxt('bindigitlabels.txt'))
X_train, X_test, y_train, y_test = train_test_split(x, labels, test_size=0.4,random_state=0)
print X_train.shape

# initialize the RBM + Logistic Regression pipeline
rbm = rbms.SKRBM()
logistic = LogisticRegression()
classifier = Pipeline([("rbm", rbm), ("logistic", logistic)])

# perform a grid search on the learning rate, number of
# iterations, and number of components on the RBM and
# C for Logistic Regression
print "SEARCHING RBM + LOGISTIC REGRESSION"
params = {
"rbm__learning_rate": [0.01, 0.1, 0.2, 0.3, 0.4, 0.5],
"rbm__n_iter": [40, 100, 300, 500],
"rbm__n_components": [10, 20, 30, 40],
"logistic__C": [100.0, 200.0, 400.]}

# perform a grid search over the parameter
start = time.time()
gs = GridSearchCV(classifier, params, n_jobs = -1, verbose = 1)
gs.fit(x, labels)

# print diagnostic information to the user and grab the
# best model
print "\ndone in %0.3fs" % (time.time() - start)
print "best score: %0.3f" % (gs.best_score_)
print "RBM + LOGISTIC REGRESSION PARAMETERS"
bestParams = gs.best_estimator_.get_params()

# loop over the parameters and print each of them out
# so they can be manually set
for p in sorted(params.keys()):
    print "\t %s: %f" % (p, bestParams[p])

# best score: 0.980
# RBM + LOGISTIC REGRESSION PARAMETERS
# 	 logistic__C: 100.000000
# 	 rbm__learning_rate: 0.300000
# 	 rbm__n_components: 30.000000
# 	 rbm__n_iter: 300.000000
