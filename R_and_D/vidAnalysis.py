"""
Vid Analysis Processor: converts vid data to a series of sound files

vid Analysis List format:
a[0] = ("1stNote",0)
a[1] = ("2ndNote",t1)
...
a[n] = ("nthNote",tn)

we want a function that takes in ti, tf, and builds a sound file that corresponds
to the video data between times ti and tf.

Note: this code does not incorporate note transitions
"""
import os
from pydub import AudioSegment
from pydubtest import play, make_chunks

def vid2SoundFile(ti,tf,vidAnalysis):
	silence = AudioSegment.from_wav("Notes/silence.wav")[500:750]
	foundTi = foundTf = False
	for i in xrange(1,len(vidAnalysis)):
		#finding where to start getting data from the analysis
		if vidAnalysis[i-1][1] <= ti <= vidAnalysis[i][1] and foundTi == False:
			indexTi = i-1
			foundTi = True
		if vidAnalysis[i-1][1] <= tf <= vidAnalysis[i][1] and foundTf == False:
			indexTf = i-1
			foundTf = True
	if foundTi == False: indexTi = len(vidAnalysis)-1
	if foundTf == False: indexTf = len(vidAnalysis)-1
	print "vidAnalysis: ", vidAnalysis
	print "indexTi = ", indexTi, " len(vidAnalysis) = ", len(vidAnalysis)
	try:
		extraBitTi = vidAnalysis[indexTi+1][1] - ti #- vidAnalysis[indexTi][1]
	except:
		extraBitTi = ti - vidAnalysis[indexTi][1]
	extraBitTf = tf - vidAnalysis[indexTf][1]
	lowerPath = "Notes/%s.wav" %vidAnalysis[indexTi][0]
	upperPath = "Notes/%s.wav" %vidAnalysis[indexTf][0]
	print os.path.exists(lowerPath)
	note = AudioSegment.from_wav(lowerPath)
	#play(note)
	lowerNote = getNote(lowerPath,extraBitTi)
	upperNote = getNote(upperPath,extraBitTf)
	#need to write getNote
	songClip = lowerNote
	# play(lowerNote)
	for i in xrange(indexTi+1,indexTf):
		notePath = "Notes/%s.wav" %vidAnalysis[i][0]
		duration = vidAnalysis[i+1][1] - vidAnalysis[i][1]
		note = getNote(notePath,duration)
		transition = getT(vidAnalysis,i)
		songClip += note.fade_in(100).fade_out(50) + transition
		# songClip += note
	return songClip + upperNote

def getT(vidAnalysis,i):
	silence = AudioSegment.from_wav("Notes/silence.wav")[500:750]
	path = "Notes/%s2%s.wav" %(vidAnalysis[i][0],vidAnalysis[i+1][0])
	if os.path.exists(path): return AudioSegment.from_wav(path)
	elif vidAnalysis[i+1] == "da": return AudioSegment.from_wav("Notes/pa2da.wav")
	else: return silence[:100]

def getNote(path,duration):
	#recursive way to get a static note of any length
	note = AudioSegment.from_wav(path)
	if 1000*duration >= len(note):
		return getNote(path,duration/2) + getNote(path,duration/2)
	else: 
		return note[:1000*duration-250]


# a = [ 
# 	 ("sa",0),
# 	 ("ri",0.5),
# 	 ("ga",1),
# 	 ("da",1.5),
# 	 ("pa",2)]

# song = vid2SoundFile(0,3,a)
# print "got song"
# # song1 = AudioSegment.from_wav("Notes/ga.wav") + AudioSegment.silent(duration=500) + AudioSegment.from_wav("Notes/pa.wav")
# play(song)




