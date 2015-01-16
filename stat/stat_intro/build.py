import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex -shell-escape stat_intro.tex")
    os.system("evince stat_intro.pdf")
    exit()
    
