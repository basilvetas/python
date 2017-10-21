import sys
import numpy as np
from numpy import linalg as LA
import scipy
import matplotlib
from matplotlib import pyplot as plt
import scipy.io as sio
from sklearn.preprocessing import normalize


## Main entry point
def main(filename):

	X, Y = loadMat(filename)	
	print(X)
	print(Y)


## Helper Methods
def loadMat(mat_file):
	mat_file = sio.loadmat(mat_file)	
	X = mat_file['X']
	Y = mat_file['Y']
	X.astype(int)
	Y.astype(int)	
	
	return X, Y



if __name__ == '__main__':	
	main(sys.argv[1])





