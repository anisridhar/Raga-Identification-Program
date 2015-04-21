#script for comparing two recordings in the time domain and frequency domain
import matplotlib.pyplot as plt
from scipy.io import wavfile # get the api
from scipy.fftpack import fft
from pylab import *
from pydub import AudioSegment
from ragas import *
from frequencyAnalysis import *
from window import window
import sys


def savePlot(f,axis,outname):
	plt.cla()
	plt.plot(axis[len(f)/3:len(f)*2/3],f[len(f)/3:len(f)*2/3])
	plt.savefig(outname)

def normalizeData(f1,axis1,f2,axis2):
	assert(len(axis1) <= len(axis2))
	newF = []
	newAxis = []
	index = 0
	for point in axis1:
		while (axis2[index] < point): index += 1
		newAxis += [axis2[index]]
		newF += [f2[index]]
	return (newF,newAxis)

def main():
	#getting two wav files from the command line
	filename1 = sys.argv[1]
	filename2 = sys.argv[2]
	(f1,axis1,fs1) = getFFT(filename1)
	(f2,axis2,fs2) = getFFT(filename2)
	if (fs1 != fs2): return False
	#plot each one, then the difference
	
	outname1 = "compare/f1.jpg"
	outname2 = "compare/f2.jpg"
	outname3 = "compare/both.jpg"
	if (len(axis1) <= len(axis2)): (f2,axis2) = normalizeData(f1,axis1,f2,axis2)
	else: (f1,axis1) = normalizeData(f2,axis2,f1,axis1) 
	print len(f1)
	print len(f2)
	savePlot(f1,axis1,outname1)
	savePlot(f2,axis2,outname2)
	f3 = [abs(f1[i]-f2[i]) for i in xrange(len(f1))]
	savePlot(f3,axis1,outname3)

main()