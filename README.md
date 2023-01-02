# ezIPC

#### create a server
```python
server = ezipc.server()
```
#### send from a server
```python
server.send(signal,data,for_)
``` 
for_ is the programID of the intened reciver (defult all)


#### create a client
```python
client = ezipc.client(**kwargs)
```
kwargs:
id (defult ""): the id of this client
time (defult 0.5): time between refreshes in seconds
