import matplotlib.pyplot as plt
from scipy.io import wavfile # get the api
from scipy.fftpack import fft
from pylab import *
from pydub import AudioSegment
from ragas import isRagam
import os



###################################################################
####################### Main Function##############################

def getMaxFrequency(filename):
	fs, data = wavfile.read(filename) # load the data
	a = data.T[0] # this is a two channel soundtrack, I get the first track
	b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
	c = fft(b) # create a list of complex number
	d = int(5000*len(c)*1.0/fs)
	fAxis = [i*fs*1.0/len(c) for i in xrange(d-1)]
	D = abs(c[:(d-1)])
	for i in xrange(d-1):
		if D[i] == max(D):
			maxF = fAxis[i]
			break
	##print "MAXF = ", maxF
	return maxF

def getNoteSequence(window,filename):
	phrase = AudioSegment.from_wav(filename)
	i = 0
	Notes = []
	while window(i+1) <= len(phrase):
		phrase[window(i):window(i+1)].export("testSong2.wav",format="wav")
		maxF = getMaxFrequency("testSong2.wav") #636 is low sa freq
		if maxF != 0:
		    note = frequencyToNote(maxF)
		    Notes += [note]
		##print note
		i += 1
	return Notes
    
def listFiles(path):
    if (os.path.isdir(path) == False):
        # base case:  not a folder, but a file, so return singleton list with its path
        return [path]
    else:
        # recursive case: it's a folder, return list of all paths
        files = [ ]
        for filename in os.listdir(path):
            files += listFiles(path + "/" + filename)
        return files

#print listFiles("/Users/vivekshankar/Documents/Raga Identifying Program")

Notes = getNoteSequence(window,"/Users/vivekshankar/Documents/Raga Identifying Program/testSong.wav"
)
print getNoteSequence(window,"/Users/vivekshankar/Documents/Raga Identifying Program/testSong.wav")
#mohanam = ["S", "R2", "G3", "P", "D2"]
#madhyamavathi = ["S", "R2", "M1", "P", "N2"]
#hindolam = ["S", "G1", "M1", "D1", "N1"]
#print isRagam(Notes,0.85,mohanam)
#print isRagam(Notes,0.8,madhyamavathi)
#print isRagam(Notes,0.5,hindolam)


#print isRagam2(Notes, 0.85, "mohanam")
#print isRagam2(Notes,0.8,"madhyamavathi")
#print isRagam2(Notes,0.6,"hindolam")

print findPosRagams(Notes, 0.85)
