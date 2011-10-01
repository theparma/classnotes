from opencv.cv import *
from opencv.highgui import *
from opencv.adaptors import Ipl2NumPy
from opencv.adaptors import Ipl2PIL
from opencv.adaptors import PIL2Ipl
import numpy as np
import Image
import lk
import math

__test__ = "/home/burak/Dropbox/Public/skfiles/campy/chessb-right.avi"
prev = None
track_x = 150
track_y = 50
__scale__ = 3
#track_x = 220
#track_y = 70
#__scale__ = 2
#track_x = 110
#track_y = 40
#__scale__ = 4
win = 5
frame_no = 0

if __name__ == '__main__':
    cvNamedWindow("Example2", CV_WINDOW_AUTOSIZE)
    capture = cvCreateFileCapture(__test__)
    loop = True
    while(loop):
        frame = cvQueryFrame(capture)
        if (frame == None): break
        gray = cvCreateImage ((frame.width, frame.height), 8, 1)   
        cvCvtColor( frame, gray, CV_BGR2GRAY )                
        ipl = Ipl2PIL(gray)
        ipl = ipl.resize((int(frame.width/__scale__),
                          int(frame.height/__scale__)), 
                         Image.ANTIALIAS)
        
        if frame_no > 25:
            curr = np.array(ipl)        
            if prev != None: 
                u, v = lk.lk(prev, curr, track_x, track_y, win)              
                print u, v
                track_x += u
                track_y += v
            prev = curr            
        
        ipl2 = PIL2Ipl(ipl)
        cvCircle(ipl2, (int(track_x), int(track_y)), 
                 2, CV_RGB(255,255,255), 0, CV_AA, 0 )   
        cvShowImage("Example2", ipl2)
        
        frame_no += 1
        
        char = cvWaitKey(33)
        if (char != -1):
            if (ord(char) == 27):
                loop = False 
                cvDestroyWindow("Example2")

