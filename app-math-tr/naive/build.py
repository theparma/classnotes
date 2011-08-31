import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex naive.tex")
    os.system("evince naive.pdf")
    exit()
    
if sys.argv[1] == 'zip':
    os.system("zip ~/Dropbox/Public/skfiles/naive.zip *.txt *.png *.py naive.tex naive.pdf")
        

