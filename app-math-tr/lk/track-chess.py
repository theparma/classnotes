from opencv.cv import *
from opencv.highgui import *
from opencv.adaptors import Ipl2NumPy
import numpy as np
import lk

prev = None
track_x = 420
track_y = 100
win = 10
__scale__ = 4

if __name__ == '__main__':
    file = "/home/burak/Dropbox/Public/skfiles/campy/chessb-right.avi"
    cvNamedWindow("Example2", CV_WINDOW_AUTOSIZE)
    capture = cvCreateFileCapture(file)
    loop = True
    __scale__ = 4
    while(loop):
        frame = cvQueryFrame(capture)
        if (frame == None): break
        gray = cvCreateImage ((frame.width, frame.height), 8, 1)   
        cvCvtColor( frame, gray, CV_BGR2GRAY )        
        curr = Ipl2NumPy(gray)
        curr = np.resize(gray,(int(frame.width/__scale__), 
                               int(frame.height/__scale__)))
        cvCircle(frame, (track_x, track_y), 
                 4, CV_RGB(0,255,0), 0, CV_AA, 0 )
                 
        if prev != None: 
            u, v = lk.lk(prev, curr, track_x, track_y, win)              
        prev = curr            
        
        cvShowImage("Example2", frame)
        
        char = cvWaitKey(33)
        if (char != -1):
            if (ord(char) == 27):
                loop = False 
                cvDestroyWindow("Example2")

