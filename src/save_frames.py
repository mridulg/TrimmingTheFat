#!/usr/bin/env python
# coding: utf-8

import cv2
from pathlib import Path

def saveFrames(img_dir,path):

	img_dir = Path(img_dir)
	#img_dir.mkdir(exist_ok=True)

	cap = cv2.VideoCapture(path)
	i=0
	while(cap.isOpened()):
	    flag, frame = cap.read()
	    if flag == False or i == 200:
	        break
	    cv2.imwrite(str(img_dir.joinpath('img_'+str(i)+'.png')), frame)
	    i+=1
	    print ("frame",i)
	print ("Executed: Stored " + str(i) + " frames")


