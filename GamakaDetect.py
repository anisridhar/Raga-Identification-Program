#script to detect where there are gamakas in an audio segment
def validInputs(freq,mags):
	#lists must be the same size
	if len(freq) == len(mags):
		print "Lists are not the same size!!"
		assert(False)
	elif len(freq) == 0:
		print "Empty Lists!"
		assert(False)

#easy scoring mechanism
def score1(f,m):
	threshold = max(m)/5
	if 1.0*sum(m)/len(m) > threshold:
		return False
	else: return True

#makes sure gradient of slope above threshold is positive before max, negative after max
def score2(f,m): pass

#input: frequency list (freq) and corresponding magnitude list (mags)
def gamakaDetect(freq,mags,getScore):
	# contract check
	validInputs(freq,mags)
	if getScore(freq,mags): return True
	else: return False


