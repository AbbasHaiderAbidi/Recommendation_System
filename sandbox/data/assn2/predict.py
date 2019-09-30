import numpy as np
from numpy import random as rand
from scipy import sparse as sps
from sklearn.datasets import load_svmlight_file
from sklearn.datasets import dump_svmlight_file

# DO NOT CHANGE THE NAME OF THIS METHOD OR ITS INPUT OUTPUT BEHAVIOR

# INPUT CONVENTION
# X: n x d matrix in csr_matrix format containing d-dim (sparse) features for n test data points
# k: the number of recommendations to return for each test data point in ranked order

# OUTPUT CONVENTION
# The method must return an n x k numpy nd-array (not numpy matrix or scipy matrix) of labels with the i-th row 
# containing k labels which it thinks are most appropriate for the i-th test point. Labels must be returned in 
# ranked order i.e. the label yPred[i][0] must be considered most appropriate followed by yPred[i][1] and so on

# CAUTION: Make sure that you return (yPred below) an n x k numpy (nd) array and not a numpy/scipy/sparse matrix
# The returned matrix will always be a dense matrix and it terribly slows things down to store it in csr format
# The evaluation code may misbehave and give unexpected results if an nd-array is not returned

def getReco( X, k ):
    # Find out how many data points we have
    n = X.shape[0]
    d = X.shape[1]
    # f=open("tst_X_Xf.txt","w")
    # f.write(str(n)+" "+str(d))

    # f.write()
    (n, d) = X.shape
    # (n1, L) = y.shape
    # assert n1 == n, "Mismatch in number of feature vectors and number of label vectors"
    dummy = sps.csr_matrix((n,1))
    dump_svmlight_file( X, dummy, "killbill.X" , multilabel = True, zero_based = True, comment = "%d %d"% (n, d) )
    f=open()
    # dump_svmlight_file( y, dummy, "%s.y" % filename, multilabel = True, zero_based = True, comment = "%d, %d" % (n, L) )
    # Load and unpack the dummy model
    # The dummy model simply stores the labels in decreasing order of their popularity
    npzModel = np.load( "model.npz" )
    model = npzModel[npzModel.files[0]]
    # Let us predict a random subset of the 2k most popular labels no matter what the test point
    shortList = model[0:2*k]
    # Make sure we are returning a numpy nd-array and not a numpy matrix or a scipy sparse matrix
    yPred = np.zeros( (n, k) )
    for i in range( n ):
        yPred[i,:] = rand.permutation( shortList )[0:k]
    return yPred