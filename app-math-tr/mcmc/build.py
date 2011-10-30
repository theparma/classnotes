import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex mcmc.tex")
    os.system("evince mcmc.pdf")
    exit()
    
    
