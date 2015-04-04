import matplotlib.pyplot as plt
from scipy.io import wavfile # get the api
from scipy.fftpack import fft
from pylab import *
import os
import math
import contextlib # for urllib.urlopen()
import urllib
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
    
    
def isRagam2(notesList, thresholdPercentage, ragam):
    #takes in a list of notes, thresholdPercentage, ragam name (string)
    #to determine whether a list of notes is a particular ragam
    ragaDict = addRagasToDict("RagaDatabase.txt")
    ragaNotes = ragaDict[ragam] #raga arohanam"
    numRagam = 0
    for note in notesList:
        if note in ragaNotes:
            numRagam += 1
    percentageRagam = numRagam*1.0/len(notesList)
    return percentageRagam >= thresholdPercentage
    
def findPosRagams(notesList, thresholdPercentage):
    ragaDict = addRagasToDict("RagaDatabase.txt")
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

def readFile(filename, mode="rt"):
    # rt = "read text"
    with open(filename, mode) as fin:
        return fin.read()

def frequencyToNote(freq):
    lowSa = 636
    a = 1.057994353 #factor to get to new notes
    k = math.log(freq*1.0/lowSa, a)
    k = int(round(k))
    notesList = (["S", "R1", "R2", "G2", "G3", 
    "M1", "M2", "P", "D1", "D2", "N2", "N3"])
    return notesList[k%12]
    
def windowFunction(n):
    timeInterval = 250 #0.5 s = 500 mS
    endTime =  n*timeInterval
    return endTime


#mohanam =  ["S", "R2", "G3", "P", "D2"]
#madhyamavathi = ["S", "R2", "M1", "P", "N2"]
#hindolam = ["S", "G1", "M1", "D1", "N1"]
