import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex -shell-escape hop*.tex")
    os.system("evince hop*.pdf")
    exit()
    
    
