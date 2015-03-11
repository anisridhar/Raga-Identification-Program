import os
import pyaudio
import pydub
from pydub import AudioSegment
"""
Support for playing AudioSegments. Pyaudio will be used if it's installed,
otherwise will fallback to ffplay. Pyaudio is a *much* nicer solution, but
is tricky to install. See my notes on installing pyaudio in a virtualenv (on 
OSX 10.10): https://gist.github.com/jiaaro/9767512210a1d80a8a0d
"""

import subprocess
from tempfile import NamedTemporaryFile
#pydub.utils import * #, get_player_name

# PLAYER = get_player_name()



# def _play_with_ffplay(seg):
# 	with NamedTemporaryFile("w+b", suffix=".wav") as f:
# 		seg.export(f.name, "wav")
# 		subprocess.call([PLAYER, "-nodisp", "-autoexit", f.name])

#make_chunks is taken from http://nullege.com/codes/search/pydub.utils.make_chunks

def make_chunks(segment,chunkLength):
	number_of_chunks = int(round((len(segment)/float(chunkLength))))
	return [segment[i*chunkLength:(i+1)*chunkLength] for i in xrange(int(number_of_chunks))]


def _play_with_pyaudio(seg):
	import pyaudio

	p = pyaudio.PyAudio()
	stream = p.open(format=p.get_format_from_width(seg.sample_width),  
                	channels=seg.channels,
	                rate=seg.frame_rate,
    	            output=True)

	# break audio into half-second chunks (to allows keyboard interrupts)
	for chunk in make_chunks(seg, 500):
		stream.write(chunk._data)

	stream.stop_stream()  
	stream.close()  

	p.terminate()  


def play(audio_segment):
	try:
		import pyaudio
		_play_with_pyaudio(audio_segment)
	except ImportError:
		_play_with_ffplay(audio_segment)

# path = "Notes/Original WAV files/highSa.wav"
# print os.path.exists(path)
# song = AudioSegment.from_wav(path)
# song = song[1500:3000]
# song1 = AudioSegment.from_wav("Notes/ma.wav")
# song2 = AudioSegment.from_wav("Notes/ga.wav")
# song3 = AudioSegment.from_wav("Notes/sa.wav")
# song = song1[1000:1500] + song1[1000:1500] + song1[1000:1500]
# play(song)
#song.export("Notes/highSa.wav",format="wav")