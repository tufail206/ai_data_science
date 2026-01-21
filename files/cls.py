# open function : HDD ------i/o stream-----RAM
#connection established using open and i/o stream
import os
dirFile=os.path.dirname(__file__)
curFile=os.path.join(dirFile,"t.txt")
try:
  f=open(curFile)
  d=f.read()
  print(d)
except FileNotFoundError as e:
  print(e)
