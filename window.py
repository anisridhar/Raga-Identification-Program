'''
WINDOW FUNCTION SPECS
All window functions must satisfy:
1. Takes in exactly one argument the file name of the audio file, which 
	determines how the file is partitioned and how many portions there are
2. Outputs a binary tuple containing:
	a. list of binary tuples (i,j), where the nth partition of the file
		is given by the nth element of the list
	b. AudioSegment object of the original file to be manipulated by the rest
		of the application
'''
from timegraphs import main
from pydub import AudioSegment

def window_time(filename,t=400):
	#t is the time interval
	phrase = AudioSegment.from_wav(filename)
	intervals = []
	i = 0
	while (i+1)*t < len(phrase):
		intervals += [(i*t,(i+1)*t)]
		i += 1
	return (intervals,phrase)

def window_timeDomain(filename): pass



#actual window function being used in application
def window(filename):
	return window_time(filename)

