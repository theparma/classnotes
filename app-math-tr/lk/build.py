import os, sys
    
if sys.argv[1] == 'zip':    
    cmd = "zip ~/Dropbox/Public/tmp/lk.zip *.m *.png " 
    os.system(cmd)
    
