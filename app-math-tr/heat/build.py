import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex heat.tex")
    os.system("evince heat.pdf")
    exit()

if sys.argv[1] == 'zip':    
    cmd = "zip ~/Dropbox/Public/skfiles/heat-fdiff.zip *.py *.pdf *.tex"
    os.system(cmd)
    
    
