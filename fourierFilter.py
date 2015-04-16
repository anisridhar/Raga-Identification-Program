#peak tracing functionality
import matplotlib.pyplot as plt
from scipy.io import wavfile # get the api
from scipy.fftpack import fft
from pylab import *
import math
from pydub import AudioSegment


#need to get time data from file and rescale it
def FFmain(filename):
	fs, data = wavfile.read(filename)
	a = data.T[0] # this is a two channel soundtrack, I get the first track
	b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
	phrase = AudioSegment.from_wav(filename)
	num_points = len(b)
	duration = len(phrase)
	time_per_point = 1.0*duration/num_points
	tAxis = [i*time_per_point for i in xrange(num_points)]
	#creating modulated function 
	cosfreq = 2000
	modFun = [b[i]*cos(2.0*math.pi*cosfreq*tAxis[i]) for i in xrange(num_points)]
	#need to take fourier transform of modFun
	c = fft(modFun) # create a list of complex number
	d = int(2000*len(c)*1.0/fs)
	fAxis = [i*fs*1.0/len(c) for i in xrange(d-1)]
	D = c[:(d-1)]
	#filtering out values greater than 2000, now need to take the inverse fourier transform
	newTimeDomain = abs(ifft(D))
	plt.cla()
	plt.plot(newTimeDomain)
	plt.savefig("PEAKTRACE_IMG.png")

FFmain("testSong.wav")