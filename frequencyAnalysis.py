#functions pertaining to audio analysis/getting frequency data, and getting data ready for note analysis

import matplotlib.pyplot as plt
from scipy.io import wavfile # get the api
from scipy.fftpack import fft
from pylab import *
from pydub import AudioSegment
from ragas import *


def getMaxFrequency(filename,noteNum):
	fs, data = wavfile.read(filename) # load the data
	a = data.T[0] # this is a two channel soundtrack, I get the first track
	b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
	c = fft(b) # create a list of complex number
	d = int(2000*len(c)*1.0/fs)
	fAxis = [i*fs*1.0/len(c) for i in xrange(d-1)]
	D = abs(c[:(d-1)])
	#want to save plots at each point
	plt.cla()
	plt.plot(fAxis,D,'r')
	#plt.show()
	#need to save plot
	plt.savefig("images2/"+ str(noteNum)+".jpg")
	for i in xrange(d-1):
		if D[i] == max(D):
			maxF = fAxis[i]
			break
	plt.cla()
	plt.plot(range(len(a)),b)
	plt.savefig("images3/"+str(noteNum)+".jpg")
	print "MAXF = ", maxF
	return maxF

def getNoteSequence(window,filename):
	phrase = AudioSegment.from_wav(filename)
	i = 0
	Notes = []
	while window(i+1) <= len(phrase):
		phrase[window(i):window(i+1)].export("testSong"+str(i)+".wav",format="wav")
		maxF = getMaxFrequency("testSong"+str(i)+".wav",i) #636 is low sa freq
		if (maxF == 0): continue
		note = frequencyToNote(maxF)
		Notes += [note]
		print note
		i += 1
	return Notes
    
def window(n,t=400):
    timeInterval = t #0.5 s = 500 mS
    endTime =  n*timeInterval
    return endTime 
"""
Notes = getNoteSequence(window,"testSong.wav")
#print getNoteSequence(window,"testSong.wav")
print Notes
mohanam = ["Sa", "Ri2", "Ga2", "Pa", "Da2"]
madhyamavathi = ["Sa", "Ri2", "Ma1", "Pa", "Ni2"]
hindolam = ["Sa", "Ga1", "Ma1", "Da1", "Ni1"]
print isRagam(Notes,0.8,mohanam)
print isRagam(Notes,0.8,madhyamavathi)
print isRagam(Notes,0.5,hindolam)
"""
