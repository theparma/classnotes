import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex eigseg.tex")
    os.system("evince eigseg.pdf")
    exit()

if sys.argv[1] == 'zip':
    os.system("zip ~/Dropbox/Public/skfiles/eigseg.zip eigseg.pdf eigseg.tex eigseg.py *.jpg *.png build.py")
    
    
