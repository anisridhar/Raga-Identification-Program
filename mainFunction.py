import matplotlib.pyplot as plt
from scipy.io import wavfile # get the api
from scipy.fftpack import fft
from pylab import *
from pydub import AudioSegment
from ragas import *
from frequencyAnalysis import *
from window import window
import sys






###################################################################
####################### Main Function##############################
print sys.argv[1]
filename = sys.argv[1]
#OPTION: only generate graphs
getMaxFrequency(filename,"TEST3")
# Notes = getNoteSequence(window,"testSong.wav")
Notes = getNoteSequence(window,filename)
#print getNoteSequence(window,"testSong.wav")
print Notes
mohanam = ["Sa", "Ri2", "Ga2", "Pa", "Da2"]
madhyamavathi = ["Sa", "Ri2", "Ma1", "Pa", "Ni2"]
hindolam = ["Sa", "Ga1", "Ma1", "Da1", "Ni1"]
# print isRagam(Notes,0.8,mohanam)
# print isRagam(Notes,0.8,madhyamavathi)
# print isRagam(Notes,0.5,hindolam)
print findPosRagams(Notes, 0.85)
