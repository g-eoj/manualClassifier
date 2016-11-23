import numpy as np
import pylab
import os
from os import listdir
from os.path import isfile, join

thumbsDirectory =  "./thumbs/";
outDirectory = "./output/";
originalsDirectory = "./originals/";
orgOutDirectory = "./orgOutput/";

def initDirectories():
	listing = [f for f in listdir(outDirectory) if not isfile(join(outDirectory, f))]
	return listing

listing = initDirectories();

def handleInt(what):
	if(what.isdigit()):
		return listing[int(what)]
	else:
		return what

def checkListing(what):
	if what not in listing:
		os.mkdir(outDirectory + what)

def showAllInListing():
	for i in range(len(listing)):
		print i,": ",listing[i]

def handleInput(currentImage, what):
	what = handleInt(what)
	checkListing(what)
	print "classified as ", what
	os.rename(thumbsDirectory + currentImage, outDirectory + what + "/" + currentImage)
	print "moved to directory ",outDirectory + what + "/" + currentImage

def main():
	for filename in os.listdir(thumbsDirectory):
		if filename.endswith(".JPG"):
			print "processing ", filename
			pylab.ion()
			img=pylab.imread(thumbsDirectory + filename);
			pylab.imshow(img);
			pylab.draw();
			showAllInListing();
			what = raw_input('what is it?');
			if(what == 'q'):
				break;
			handleInput(filename, what)

main()



