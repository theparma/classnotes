import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex buyuk.tex")
    os.system("evince  buyuk.pdf")
    exit()

if sys.argv[1] == 'zip':    
    cmd = "zip ~/Dropbox/Public/skfiles/buyuk.zip buyuk.pdf buyuk.tex build.py"
    os.system(cmd)
