import matplotlib.pyplot as plt
from scipy.io import wavfile # get the api
from scipy.fftpack import fft
from pylab import *

def findBreaks2 (b,plt):
	data = [abs(e)-50 for e in b]


def findBreaks(b,plt):
	data = [abs(e)-50 for e in b]
	#find set of points below 0
	minPoints = []
	for i in xrange(len(data)):
		if data[i] < 0: minPoints += [i]
	for i in xrange(0,len(data),1000):
		for a in xrange(max(0,i-50),min(len(data),i+50)):
			if a not in minPoints:
				foundVal = False
				break
			foundVal = True
		if foundVal:
			plt.plot([i]*500,range(500),'r')

def getTimePlots(filename,noteNum):
	fs, data = wavfile.read(filename)
	a = data.T[0] # this is a two channel soundtrack, I get the first track
	b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
	#starting to graph it 
	c = [abs(e) for e in b]
	plt.cla()
	plt.plot(range(len(a)),c,'b')
	findBreaks(b,plt)
	plt.savefig("images3/FULL_"+str(noteNum)+".jpg")

def main(filename):
	getTimePlots(filename,0)

main("testSong.wav")