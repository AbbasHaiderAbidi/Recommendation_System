import numpy as np
from numpy import random as rand
from scipy import sparse as sps
from sklearn.datasets import load_svmlight_file
from sklearn.datasets import dump_svmlight_file

def dump_food( matrix_test, in_path, out_path):
	(n, d) = matrix_test.shape
	dummy = sps.csr_matrix( (n, 1) )
	dump_svmlight_file( matrix_test, dummy, "test_data.X", multilabel = True, zero_based = True, comment = "%d %d" % (n, d) )	

	test_ws=open("test_data.X","r")
	y_is=open("../eurlex/tst_X_Y.txt","w")

	for i in range(0,3):
		test_ws.readline();	

	lines=test_ws.readlines()

	lines[0]=lines[0][2:]
	test_is.write(lines[0])
	for i in range(1,len(lines)):
		lines[i]=lines[i][1:]
		test_is.write(lines[i])

	test_is.close()


# d = 16385
# L = 3400

# X, _ = load_svmlight_file( "data.X", multilabel = True, n_features = d, offset = 1 )
# y, _ = load_svmlight_file( "data.y", multilabel = True, n_features = L, offset = 1 )

# 

# dummy = sps.csr_matrix( (n, 1) )
# dump_svmlight_file( X, dummy, "data_dump.X", multilabel = True, zero_based = True, comment = "%d %d" % (n, d) )
# dump_svmlight_file( y, dummy, "data_dump.y", multilabel = True, zero_based = True, comment = "%d %d" % (n1, L) )

# y_ws=open("data_dump.y","r")
# y_is=open("../eurlex/trn_X_Y.txt","w")

# for i in range(0,3):
# 	y_ws.readline();	

# lines=y_ws.readlines()

# lines[0]=lines[0][2:]
# y_is.write(lines[0])
# for i in range(1,len(lines)):
# 	lines[i]=lines[i][1:]
# 	y_is.write(lines[i])

# y_is.close()

# x_ws=open("data_dump.X","r")
# x_is=open("../eurlex/trn_X_Xf.txt","w")

# for i in range(0,3):
# 	x_ws.readline();	


# lines=x_ws.readlines()

# lines[0]=lines[0][2:]
# x_is.write(lines[0])
# for i in range(1,len(lines)):
# 	lines[i]=lines[i][1:]
# 	x_is.write(lines[i])

# x_is.close()
