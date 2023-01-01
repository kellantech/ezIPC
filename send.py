import time
def send(msg,data):
  id = int(time.time())
  l = f"{id}:{msg}:{data}\n"

  with open("df.txt","a") as df:
    df.write(l)
    df.flush()

