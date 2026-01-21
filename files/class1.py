# file , two types 
# 1 text form where data exist in the for of text

# binary file like mp4,mov , .png
# both data store in system like 0,1

import os 
dirFile=os.path.dirname(__file__)
curFile=os.path.join(dirFile,"t.txt")

with open(curFile,"r",encoding="utf-8")as f:
    print(f.read())