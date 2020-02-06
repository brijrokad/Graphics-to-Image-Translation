##############################################################################################
#author: BRIJ ROKAD
#updated: 02/06/2020
##############################################################################################

import os
import cv2
from tqdm import tqdm
#from natsort import natsorted

destination = "/home/br54772/THEA 7780/Data/"	# URL for the destination of frames
source = "/home/br54772/THEA 7780/Data/"	# URL for the source of clips
srcfiles = os.listdir(source)

# Filter the files from srcfiles. srcfiles is list of all files presented in the source directory.
# Suppose you only want the ".mp4" files and don't need and ".txt" files which are presented in source directory.
# The function file.endswith("desired file extention") in this case it's mp4 will select only files which are ended with ".mp4"

def fileFilter(sourcelist):
    srclist = []
    for file in sourcelist:
        if file.endswith(".mp4"):
            srclist.append(file)
            
    srclist = sorted(srclist)
    #srclist = natnatsorted(srclist)
    # If your clips are named numerically then use natsorted function (remove # from line 9 and line 26).
    
    return srclist

videolist = fileFilter(srcfiles)

# clipname[:-4] will take the original filename disragarding last 4 characters
# For example clipname is "closeup_1.mp4" then clipname[:-4] will closeup_1
# let's say our current count is 7
# destination+clipname[:-4]+"_"+str(count)+".jpg" --> "/home/brijrokad/THEA 7780/Data/Frames/Real/closeup_1_7.jpg"
def getFrame(sec, destination, clipname):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames, image = vidcap.read()
    if hasFrames:
        cv2.imwrite(destination+clipname[:-4]+"_"+str(count)+".jpg", image) # save the frame as JPG file
    return hasFrames

sec = 0
frameRate = 30 # It'll capture a frame in each x second, 1000 miliseconds = 1 second so if we want 30 fps then 30/1000 = 0.03.
count = 1

for clip in tqdm(videolist):
    vidcap = cv2.VideoCapture(source+clip)
    success = getFrame(sec, destination, clip)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec, destination, clip)