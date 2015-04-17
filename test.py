import matplotlib.pyplot as plt
from scipy.io import wavfile # get the api
from scipy.fftpack import fft
from pylab import *
from pydub import AudioSegment
from pydubtest import play

# file1 = AudioSegment.from_wav('ri.wav')
# file2 = AudioSegment.from_wav('sa.wav')
# song = file1[:1000] + file2[:1000]

# song = AudioSegment.from_wav("mohanamPhrase1.wav")

song = AudioSegment.from_wav('Hamsanadam_ar_av.wav')
play(song)
# play(song[1500:4000])
# play(song[4500:8000])
# play(song[8500:11000])

# song = AudioSegment.from_wav('mohanamPhrase2.wav')[5500:8000]
# play(song[1000:5000])
# play(song[5500:8000])


song.export("testSong.wav",format="wav")

# print data1

# fs, data = wavfile.read('testSong.wav') # load the data
# a = data.T[0] # this is a two channel soundtrack, I get the first track
# b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
# c = fft(b) # create a list of complex number
# d = len(c)/2  # you only need half of the fft list
# d = int(5000*len(c)*1.0/fs)
# fAxis = [i*fs*1.0/len(c) for i in xrange(d-1)]
# k = max(abs(c[:(d-1)]))
# D = abs(c[:(d-1)])
# maxLine = [max(abs(c[:(d-1)]))]*(d-1)
# plt.plot(fAxis,abs(c[:(d-1)]),'r') 
# plt.plot(fAxis,maxLine,"b")
# for i in xrange(d-1):
# 	if D[i] == max(D):
# 		maxF = fAxis[i]
# 		break
# A = 1.057994353
# baseNote = 636




plt.show()
