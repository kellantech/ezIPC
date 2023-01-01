import time

_clid_ = 0

def get(tm=0.5):
  global _clid_
  time.sleep(tm)
  with open("df.txt")as df:cv=df.read().split("\n")
  cvs = cv[-2].split(":")
  cid =int(cvs[0])
  if cid>_clid_:
    _clid_=cid
    cmg = cvs[1]
    cda = cvs[2]
    return cmg,cda
  
  return '',''
