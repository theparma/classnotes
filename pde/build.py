import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdftk pde*/pde*.pdf output ~/Dropbox/Public/skfiles/pde.pdf")
    exit()
    
    
