import matplotlib.pyplot as plt
from scipy.io import wavfile # get the api
from scipy.fftpack import fft
from pylab import *
from pydub import AudioSegment
from ragas import isRagam
import os

################################
#### Ragas.py functions ########
################################

def readFile(filename, mode="rt"):
    # rt = "read text"
    with open(filename, mode) as fin:
        return fin.read()

def addRagasToDict(textfile):
    #returns dictionary
    #maps raga name to list containing its constituent notes (only Arohanam)
    ragaDict = dict()
    text = readFile(textfile)
    ragaList = text.splitlines()
    for raga in ragaList:
        nameStartIndex = raga.index("|")
        nameEndIndex = raga.index("|",nameStartIndex+1)
        name = raga[nameStartIndex+1:nameEndIndex].strip()
        notes = raga[nameEndIndex+1:].strip()
        notesList = notes.split()
        #G1 should become R2
        #N1 should become D2
        for i in xrange(len(notesList)):
            if notesList[i] == 'G1':
                notesList[i] = 'R2'
            elif notesList[i] == 'N1':
                notesList[i] = 'D2'
        ragaDict[name] = notesList
    return ragaDict

def frequencyToNote(freq):
    lowSa = 636
    a = 1.057994353 #factor to get to new notes
    k = math.log(freq*1.0/lowSa, a)
    k = int(round(k))
    notesList = (["S", "R1", "R2", "G2", "G3", 
    "M1", "M2", "P", "D1", "D2", "N2", "N3"])
    return notesList[k%12]
    
def windowFunction(n):
    timeInterval = 500 #0.5 s = 500 mS
    endTime =  n*timeInterval
    return endTime
    
def isRagam2(notesList, thresholdPercentage, ragam):
    #takes in a list of notes, thresholdPercentage, ragam name (string)
    #to determine whether a list of notes is a particular ragam
    ragaDict = addRagasToDict("/Users/vivekshankar/Documents/Raga Identifying Program/RagaDatabase.txt")
    ragaNotes = ragaDict[ragam] #raga arohanam"
    numRagam = 0
    for note in notesList:
        if note in ragaNotes:
            numRagam += 1
    percentageRagam = numRagam*1.0/len(notesList)
    return percentageRagam >= thresholdPercentage
    
def findPosRagams(notesList, thresholdPercentage):
    ragaDict = addRagasToDict("/Users/vivekshankar/Documents/Raga Identifying Program/RagaDatabase.txt")
    posRagas = []
    for ragam in ragaDict:
        ragaNotes = ragaDict[ragam]
        numRagam = 0
        for note in notesList:
            if note in ragaNotes:
                numRagam += 1
        percentageRagam = numRagam*1.0/len(notesList)
        if percentageRagam >= thresholdPercentage:
            posRagas += [ragam]
    return posRagas

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

def frequencyToNote(freq):
    lowSa = 636
    a = 1.057994353 #factor to get to new notes
    ##print freq
    k = math.log(freq*1.0/lowSa, a)
    k = int(round(k))
    notesList = (["S", "R1", "R2", "G2", "G3", 
    "M1", "M2", "P", "D1", "D2", "N2", "N3"])
    return notesList[k%12]
    
def window(n,t=250):
    timeInterval = t #0.5 s = 500 mS
    endTime =  n*timeInterval
    return endTime 
    
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
