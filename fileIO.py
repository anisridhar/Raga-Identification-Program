
def writeFile(contents,filename,mode="wt"):
	with open(filename,mode) as fout:
		fout.write(contents)

def readFile(filename,mode="rt"):
	with open(filename,mode) as fin:
		return fin.read()

def addInfo(contents,filename):
	#get existing contents
	currentData = readFile(filename)
	newData = currentData + contents
	writeFile(contents,filename)
	
