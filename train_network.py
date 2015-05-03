'''
Script to write data from audio files and convert them into format to 
train neural network. 
'''
from fileIO import *
from frequencyAnalysis import *
import numpy as np


def writeData(i=10):
	gamakas = ["ma","ri"]
	freqs = None
	for g in gamakas:
		for k in xrange(i):
			filename = "SANK_PHRASES/" + g + str(k) + ".wav"
			(D,faxis,fs) = getFFT(filename,15000)
			if (freqs != None and freqs != fs):
				print "freqs = ", freqs
				return;
			else: freqs = fs
			#need to normalize the data
			D = normalize(D)
			#now need to save the data
			contents = ""
			for data in D:
				contents += str(data) + "\n"
			target_filename = "FDATA/" + g + "/" + str(k) + ".txt"
			writeFile(contents,target_filename)
		print "Finished data write for " + g + "!"

def normalize(a):
	maxVal = max(a)
	newA = [1.0*a[i]/max(a) for i in xrange(len(a))]
	return newA

def readData(i=10):
	gamakas = ["ma","ri"]
	gData = [[1,0],[0,1]]
	training_data = []
	# contents = readFile("FDATA/ma/0.txt")
	# print contents
	for g in xrange(len(gamakas)):
		for k in xrange(i):
			filename = "FDATA/" + gamakas[g] + "/" + str(k) + ".txt"
			contents = readFile(filename)
			# print type(contents)
			contents = contents.splitlines()
			# print contents[0]
			# print float(contents[0])
			data = [float(val) for val in contents]
			data = np.asarray(data)
			training_data += [(data,gData[g])]
	print len(data)
	return training_data




# writeData(10)

