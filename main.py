import time

_clid_ = 0

def send(msg,data):
  id = int(time.time())
  l = f"{id}:{msg}:{data}\n"

  with open("df.txt","a") as df:
    df.write(l)
    df.flush()

def get(tm=0.5):
  global _clid_
  time.sleep(tm)
  with open("df.txt") as df:
    cv=df.read().split("\n")
  ccid=_clid_
  evnts = []
  for ln in cv:  
    if ln=="":continue
    cvs = ln.split(":")
    cid =int(cvs[0])
    if cid>_clid_:
      if cid>ccid:
        ccid=cid
      cmg = cvs[1]
      cda = cvs[2]
      evnts.append([cmg,cda])
  _clid_=ccid 
  return evnts

def clear():
  with open("df.txt","w")as cf2:
    cf2.write("")
