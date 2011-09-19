import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdftk calc_multi*/*.pdf output ~/Dropbox/Public/skfiles/multivar_calculus.pdf")
    exit()
    
    
