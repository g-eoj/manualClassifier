import numpy as np
import pylab
import os
import sys
from os import listdir
from os.path import isfile, join

outDirectory = "./output/";
inDirectory = sys.argv[1];
cameraName = "UpperTrailCamera";
offset = 0;
listing = []

def initDirectories():
	global listing
	listing = [f for f in listdir(outDirectory) if not isfile(join(outDirectory, f))]
	listing.sort()
	return listing

listing = initDirectories();
print "loading listing ", listing

def handleInt(what):
	global listing
	if(what.isdigit()):
		return listing[int(what)]
	else:
		return what

def checkListing(what):
	global listing
	if what not in listing:
		os.mkdir(outDirectory + what)

def showAllInListing():
	global listing
	for i in range(len(listing)):
		print i,": ",listing[i]

def handleInput(currentImage, what):
	global listing
	what = handleInt(what)
	checkListing(what)
	listing = initDirectories();
	print "classified as ", what
        name = outDirectory + what + "/" + cameraName + "_" + currentImage
	os.rename(inDirectory + currentImage, name)
	print "moved to directory ",name

def main():
	print "getting filename list..."
	filenames = os.listdir(inDirectory)
	print "sorting filenames"
	filenames.sort()
	index = offset-1;
	while index < len(filenames):
		index = index + 1
		print "filename index ", index
		filename = filenames[index];
		if filename.endswith(".JPG"):
			print "processing ", filename
			pylab.ion()
			img=pylab.imread(inDirectory + filename);
			pylab.imshow(img);
			pylab.draw();
			showAllInListing();
			what = raw_input('what is it? ');
			if(what == 'q'):
				break;
			elif(what == 'n'):
				print "right arrow"
				continue;
			elif(what == 'b'):
				print "left arrow"
				index = index - 2;
				continue;
			handleInput(filename, what)

main()




