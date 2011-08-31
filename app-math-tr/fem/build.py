import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex fem.tex")
    os.system("evince fem.pdf")
    exit()

if sys.argv[1] == 'zip':
    os.system("zip ~/Dropbox/Public/skfiles/fem.zip fem_hat.png fem.py fem.tex fem.pdf build.py")
    
    
