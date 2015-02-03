import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex -shell-escape pcd.tex")
    os.system("evince pcd.pdf")
    exit()
