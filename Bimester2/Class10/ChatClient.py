#!/usr/bin/python3

from socket import *
import threading


# Defaults local host
HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
name = ''


# Socket initialization
tcpCliSock = socket(AF_INET, SOCK_STREAM)
ADDR = (HOST, PORT)
tcpCliSock.connect(ADDR)
host=tcpCliSock.getsockname()

# Boolean to format enters
enter = True


def listener():
    """Method for listening to new messages"""

    global enter, name

    # First data
    data = tcpCliSock.recv(BUFSIZ)
    print(data.decode('utf-8'))

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        if enter:
            print(data.decode('utf-8') + "\n" + name + ">")
            enter = False
        else:
            print(data.decode('utf-8') + "\n" + name + ">")


if __name__ == "__main__":

    threading.Thread(target=listener).start()

    first_input = True

    while True:
        if first_input:
            name = input()
            data = name.encode('utf-8')
            first_input = False
        else:
            data = (input('%s>\n' % name)).encode('utf-8')
            enter = True
        if not data:
            break
        tcpCliSock.send(data)
    tcpCliSock.close()
