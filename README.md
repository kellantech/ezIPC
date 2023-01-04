# !! THESE ARE OLD DOCS !! NEW ONES COMING SOON !!

# ezIPC

### install
`pip install ezipc`

##### import
`import ezipc`

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
id (defult no ID): the id of this client  
time (defult 0.5): time between refreshes in seconds

`client.get()`

return a list of all \[signal,data\] pairs in list format

`client.clear()`

Clears log

recomended to call at end of program
