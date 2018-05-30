#!/usr/bin/python3

import socket
import threading
from time import ctime

# The default port for the server
PORT = 21567


class ChatServer(object):
    def __init__(self, host, port):
        """
        Initialization for the server
        """
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.messagesList = []
        self.connected = []

    def listen(self):
        """
        Loop for accepting clients
        """
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(3000)
            client_thread = threading.Thread(target=self.listenToClient, args=(client, address))
            client_thread.start()

    def listenToClient(self, client, address):
        """Client thread method"""

        # max message size
        size = 1024

        # Getting client's name
        client.send('Please type your name: '.encode('utf-8'))
        name = str(client.recv(size)).strip('b').strip('\' ')
        print(name, "connected.")
        self.connected.append(name)

        # Message dispatcher thread
        dispatcher = threading.Thread(target=self.writeDataToClient, args=(client, name))
        dispatcher.start()

        while True:
            try:
                data = client.recv(size)
                if data:
                    str_data = data.decode('utf-8')
                    str_data = name + ">" + str_data
                    print(str_data)
                    self.messagesList.append([str_data.encode('utf-8'), name])
                else:
                    self.connected.remove(name)
                    raise Exception('Client disconnected')

            except:
                client.close()
                print("%s disconnected." % name)
                return False

    def writeDataToClient(self, client, name):
        """This method is responsible for writing data to the clients"""

        index = len(self.messagesList)

        while name in self.connected:
            if len(self.messagesList) > index:
                if self.messagesList[index][1] != name:
                    client.send(self.messagesList[index][0])
                    index += 1
                else:
                    index += 1


if __name__ == "__main__":
    while True:
        port_num = PORT
        try:
            port_num = int(port_num)
            break
        except ValueError:
            pass

    try:
        print("Server launched on port %d, press CONTROL-C to finish the server..." % port_num)
        ChatServer('', port_num).listen()
    except:
        print("Closing the server...")
