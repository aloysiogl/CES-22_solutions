#!/usr/bin/python3

from socket import *
import threading


# Defaults local host
HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024

tcpCliSock = socket(AF_INET, SOCK_STREAM)
ADDR = (HOST, PORT)
tcpCliSock.connect(ADDR)
host=tcpCliSock.getsockname()


def listener():
    """Method for listening to new messages"""
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print(data.decode('utf-8'))


if __name__ == "__main__":

    threading.Thread(target=listener).start()

    first_input = True
    name = ''

    while True:
        if first_input:
            name = input()
            data = name.encode('utf-8')
            first_input = False
        else:
            data = (input('%s> ' % name)).encode('utf-8')
        if not data:
            break
        tcpCliSock.send(data)
    tcpCliSock.close()
