'''
WINDOW FUNCTION SPECS
All window functions must satisfy:
1. Takes in exactly one argument (the audioSegment object phrase) which 
	determines how the file is partitioned and how many portions there are
2. Outputs a list of binary tuples (i,j), where the nth partition of the file
	is given by the nth element of the list
'''

def window_time(phrase,t=400):
	#t is the time interval
	intervals = []
	i = 0
	while (i+1)*t < len(phrase):
		intervals += [(i*t,(i+1)*t)]
		i += 1
	return intervals

#actual window function being used in application
def window(phrase):
	return window_time(phrase)

