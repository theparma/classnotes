import os, sys

if sys.argv[1] == 'zip':
    os.system("zip %s/Downloads/mr_rnd_svd_0.2.zip *.py *.csv *matrix* " % os.environ['HOME'])
