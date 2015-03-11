import numpy as np
import random

def generateNotes(length):
	n = length
	(p1,p2,p3) = (0.375,0.425,0.525)
	(pg,pd,pp) = (1-(p1+p2),1-(p1+p3),1-(p2+p3))
	T = np.matrix([[pg,p1,p2],[p1,pd,p3],[p2,p3,pp]])
	init = np.matrix([[1],[0],[0]])
	noteString = ""
	for i in xrange(n):
		init = T*init
		probList = ["G"]*(int(round(1000*init[0][0])))+["D"]*(int(round(1000*init[1][0])))+["P"]*(int(round(1000*init[2][0])))
		random.shuffle(probList)
		noteString += probList[random.randint(0,999)]
	print noteString


generateNotes(10)