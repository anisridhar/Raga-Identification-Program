import matplotlib.pyplot as plt
from scipy.io import wavfile # get the api
from scipy.fftpack import fft
from pylab import *

def getAverage(bp):
	difList = [(bp[i+1]-bp[i]) for i in xrange(len(bp)-1)]
	return (difList,sum(difList)/len(difList))

def getInterval(bp,data):
	intervalList = []
	(difList,av) = getAverage(bp)
	for i in xrange(len(bp)-1):
		if difList[i] > av: intervalList += [(bp[i],bp[i+1])]
	return (intervalList,len(data))

def getInterval2(bp,data):
	intervalList = []
	for i in xrange(len(bp)-1):
		if max(data[bp[i]:bp[i+1]]) > 0: intervalList += [(bp[i],bp[i+1])]
		# samplePt = (bp[i] + bp[i+1])/2
		# if data[samplePt] > 0: intervalList += [(bp[i],bp[i+1])]
	return (intervalList,len(data))

def findBreaks(b,plt):
	data = [abs(e)-50 for e in b]
	#find set of points below 0
	minPoints = []
	boundaryPoints = []
	# for i in xrange(len(data)):
	# 	if data[i] < 0: minPoints += [i]
	for i in xrange(0,len(data),1000):
		for a in xrange(max(0,i-10),min(len(data),i+10)):
			if data[a]>0:
				foundVal = False
				break
			foundVal = True
		if foundVal:
			plt.plot([i]*500,range(500),'r')
			boundaryPoints += [i]
	return getInterval(boundaryPoints,data)

def getTimePlots(filename,noteNum):
	fs, data = wavfile.read(filename)
	a = data.T[0] # this is a two channel soundtrack, I get the first track
	b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
	#starting to graph it 
	c = [abs(e) for e in b]
	plt.cla()
	plt.plot(range(len(a)),c,'b')
	databundle = findBreaks(b,plt)
	plt.savefig("images3/FULL_"+str(noteNum)+".jpg")
	return databundle


def main(filename):
	return getTimePlots(filename,0)

# print main("testSong.wav")