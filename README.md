# Local chat

Usage:

- Run server.py, create a socket by entering the IP address and port number.
- Run client.py, connect to the socket with the same details entered in server.py

Issues may come up when trying to enter addresses not known by your computer.

You can resolve this by entering `ipconfig` into your terminal and check your computers IP address use that to start the server or connect with it.

server.py example:
```
python .\server.py
Enter address: 0.0.0.0
Enter port number: 12345
Server has started
```

client.py example:
```
python .\client.py
Enter an IP address: 0.0.0.0
Enter port number: 12345
Client socket created
```
