import matplotlib.pyplot as plt
from scipy.io import wavfile # get the api
from scipy.fftpack import fft
from pylab import *
import os
import math
#from pydub import AudioSegment

#file1 = AudioSegment.from_wav('ri.wav')
#file2 = AudioSegment.from_wav('sa.wav')
#song = file1[:250] + file2[:500]
#song.export("testSong.wav",format="wav")

# print data1

#def listFiles(path):
#    if (os.path.isdir(path) == False):
#        # base case:  not a folder, but a file, so return singleton list with its path
#        return [path]
#    else:
#        # recursive case: it's a folder, return list of all paths
#        files = [ ]
#        for filename in os.listdir(path):
#            files += listFiles(path + "/" + filename)
#        return files
#        
# To test this,x download and expand this zip file in the same directory
# as the Python file you are running:  sampleFiles.zip
#
#print listFiles("/Users/vivekshankar/Documents/Raga Identifying Program")

# fs, data = wavfile.read('/Users/vivekshankar/Documents/Raga Identifying Program/testSong.wav') # load the data
# a = data.T[0] # this is a two channel soundtrack, I get the first track
# b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
# c = fft(b) # create a list of complex number
# d = len(c)/2  # you only need half of the fft list
# d = int(5000*len(c)*1.0/fs)
# fAxis = [i*fs*1.0/len(c) for i in xrange(d-1)]
# plt.plot(fAxis,abs(c[:(d-1)]),'r') 
# plt.show()

def frequencyToNote(freq):
    lowSa = 636
    a = 1.057994353 #factor to get to new notes
    k = math.log(freq*1.0/lowSa, a)
    k = int(round(k))
    notesList = (["Sa", "Ri1", "Ri2", "Ga1", "Ga2", 
    "Ma1", "Ma2", "Pa", "Da1", "Da2", "Ni1", "Ni2"])
    return notesList[k%12]
    
def windowFunction(n):
    timeInterval = 500 #0.5 s = 500 mS
    endTime =  n*timeInterval
    return endTime

def isRagam(notesList, thresholdPercentage, ragam):
    #takes in a list of notes, thresholdPercentage 
    #to determine whether list of notes is "Mohanam"
    numRagam = 0
    for note in notesList:
        if note in ragam:
            numRagam += 1
    percentageMohanam = numRagam*1.0/len(notesList)
    return percentageMohanam >= thresholdPercentage

#mohanam = ["Sa", "Ri2", "Ga2", "Pa", "Da2"]
#madhyamavathi = ["Sa", "Ri2", "Ma1", "Pa", "Ni2"]
#hindolam = ["Sa", "Ga1", "Ma1", "Da1", "Ni1"]