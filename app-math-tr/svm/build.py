import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex svm.tex")
    os.system("evince svm.pdf")
    exit()
    
if sys.argv[1] == 'zip':    
    cmd = "zip ~/Dropbox/Public/skfiles/svm-tr.zip build.py *.tex *.pdf *.png *.py"
    os.system(cmd)
    
