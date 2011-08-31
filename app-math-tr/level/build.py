import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex level.tex")
    os.system("evince level.pdf")
    exit()        
if sys.argv[1] == 'zip':
    os.system("zip ~/Dropbox/Public/skfiles/level-set-edge.zip level.pdf level.tex *.m *.py *.bmp pics/*")

