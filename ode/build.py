import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdftk */ode*.pdf output ~/Dropbox/Public/skfiles/ode_mattuck.pdf")
    exit()
    
    
