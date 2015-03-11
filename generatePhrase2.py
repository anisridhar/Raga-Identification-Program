import numpy as np
import random

def generateNotes(length):
	pf = ps = 1/2
	T = np.matrix([[0,0,0.5],[0.5,0,0.5],[0.5,1,0]])
	# init = np.matrix([[0],[0],[1]])
	# print "init ",T*init
	notes = ["G","P","D"]
	noteString = notes[random.randint(0,2)]
	for i in xrange(length):
		if noteString[-1] == "G": init = np.matrix([[1],[0],[0]])
		elif noteString[-1] == "D": init = np.matrix([[0],[1],[0]])
		else: init = np.matrix([[0],[0],[1]])
		probs = T*init
		if noteString[-1] == "D": print probs
		probList = ["G"]*(int(round(1000*probs[0][0])))+["D"]*(int(round(1000*probs[1][0])))+["P"]*(int(round(1000*probs[2][0])))
		# random.shuffle(probList)
		noteString += probList[random.randint(0,len(probList))]
		if len(noteString) >= 2 and noteString[-1] == noteString[-2]: print probs
	print noteString

generateNotes(4)