import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex stat*.tex")
    os.system("evince stat*.pdf")
    exit()
    
