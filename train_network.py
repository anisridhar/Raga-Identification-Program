'''
Script to write data from audio files and convert them into format to 
train neural network. 
'''
from fileIO import *
from frequencyAnalysis import *
import numpy as np


def writeData1(i=10):
	gamakas = ["ma","ri"]
	freqs = None
	maxfreq = 15000
	for g in gamakas:
		for k in xrange(i):
			filename = "SANK_PHRASES/" + g + str(k) + ".wav"
			(D,faxis,fs) = getFFT(filename,maxfreq)
			# print faxis
			# print "fs = ", fs
			#need to normalize the data
			D = normalize(D,faxis,maxfreq)
			#now need to save the data
			contents = ""
			for data in D:
				contents += str(data) + "\n"
			target_filename = "FDATA/" + g + "/" + str(k) + ".txt"
			writeFile(contents,target_filename)
			print "Finished data write for " + g + str(k) + "!"

def writeData_test(i=10):
	gamakas = ["ma","ri"]
	freqs = None
	for g in gamakas:
		for k in xrange(i):
			filename = "SANK_PHRASES/" + g + str(k) + ".wav"
			(D,faxis,fs) = getFFT(filename,15000)
			print "fs = ", fs
			print len(D)

def writeData2(i=10):
	gamakas = ["ma","ri"]
	freqs = None
	contents = ""
	out_data = ""
	for g in gamakas:
		for k in xrange(i):
			filename = "SANK_PHRASES/" + g + str(k) + ".wav"
			(D,faxis,fs) = getFFT(filename,15000)
			if (freqs != None and freqs != fs):
				print "freqs = ",freqs
				return;
			else: freqs = fs
			D = normalize(D)
			for data in D:
				contents += str(data) + " "
			contents += "\n"
			if g == "ma": out_data += "1 0\n"
			else: out_data += "0 1\n"
			# target_filename = "freqData/" + g + "/" + str(k) + ".txt"
			# writeFile(contents,target_filename)
		print "Finished data write for " + g + "!"
	writeFile(contents,"freqData/trainIN.txt")
	writeFile(out_data,"freqData/trainOUT.txt")

def writeData(i=10):
	gamakas = ["ma","ri"]
	freqs = None
	in_data = ""
	out_data = ""
	for g in gamakas:
		for k in xrange(i):
			filename = "FDATA/" + g + "/" + str(k) + ".txt"
			contents = readFile(filename).splitlines()
			for val in contents:
				in_data += val + " "
			in_data = in_data[:-1] + "\n"
			if g == "ma": out_data += "1 0\n"
			else: out_data += "0 1\n"
	writeFile(in_data,"FDATA/trainIN.txt")
	writeFile(out_data,"FDATA/trainOUT.txt")


def normalize(a,axis,maxfreq):
	maxVal = max(a)
	newA = []
	#need to resize array
	i = 0
	for j in xrange(len(axis)):
		if (i >= maxfreq-1): break
		if (axis[j] >= i):
			newA += [a[i]*1.0/maxVal]
			i += 1


		# for i in xrange(maxfreq):
		# 	print i
		# 	if (axis[j] >= i):
		# 		newA += [a[i]*1.0/maxVal]
		# 		continue
	# newA = [1.0*a[i]/max(a) for i in xrange(len(a))]
	print "length of resized array is...", len(newA)
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

def readSize(filename):
	contents = readFile(filename).splitlines()
	print "number of samples: ", len(contents)
	for i in xrange(20):
		print "Number of data points for " + str(i) + ": ", len(contents[i].split(" "))

def makeTest(i):
	contents = readFile("FDATA/trainIN.txt").splitlines()[i]
	writeFile(contents,"FDATA/testIN.txt")

makeTest(5)
# writeData()
# readSize("FDATA/trainIN.txt")



# writeData()
