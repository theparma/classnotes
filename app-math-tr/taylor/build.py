import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex taylor.tex")
    os.system("evince taylor.pdf")
    exit()

if sys.argv[1] == 'zip':
    os.system("zip ~/Dropbox/Public/skfiles/taylor.zip taylor.tex taylor.pdf build.py")
