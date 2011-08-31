import os, sys

import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex fourier.tex")
    os.system("evince fourier.pdf")
    exit()
    
if sys.argv[1] == 'zip':
    os.system("zip ~/Dropbox/Public/skfiles/fourier.zip build.py fourier-fn.png fourier.pdf fourier.py fourier.tex sunspots.dat sunspots-fourier.png")
    
    
