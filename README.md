# ezIPC

### install
`pip install ezipc`

##### import
`import ezipc`

#### create a client
```python
client = ezipc.client(channel,**kwargs)
```
channel (defult "main"): what channel to communicate on

kwargs:  
id (defult no ID): the id of this client  
time (defult 0.5): time between refreshes in seconds

`clent.send(event,data,for_)`  
for_ is the programID of the intened reciver (defult all)

`client.get()`  
return a list of all \[event,data\] pairs in list format


`client.add_handler(event,handler)`  
adds a handler to be called when client recives event `event`

`client.handler_listen(quit=True)`  
listens for events, and calles handler when necessary  

quit (defult True): break on event `QUIT`
