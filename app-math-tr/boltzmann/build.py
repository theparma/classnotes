import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex -shell-escape bol*.tex")
    os.system("evince bol*.pdf")
    exit()
    
    
