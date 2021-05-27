# Port Scanner implementation in Java

Python Port Scanner script I did in order to check all the ports that are on my *localhost*. I used the socket module in Python3 in order to try and connect to a port, If the connection fails I consider the port to be closed.

- The default *target* is '127.0.0.1' but can be changed to the user input
- The default ports to be scanned are the reserved ports on a computer (first 1024). This can be changed to user input given in the form of `startPortNumber-endPortNumber`

## Port and vulnerability scanning of a target without permission is **NOT OK**!
