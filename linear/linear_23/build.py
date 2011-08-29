import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex linear_*.tex")
    os.system("evince linear_*.pdf")
    exit()
    
if sys.argv[1] == 'zip':    
    cmd = "zip ~/Dropbox/Public/skfiles/linear/linear_%d.zip linear_%d.tex linear_%d.pdf *.png *.py" % \
        (int(sys.argv[2]), int(sys.argv[2]), int(sys.argv[2]))
    os.system(cmd)
    
