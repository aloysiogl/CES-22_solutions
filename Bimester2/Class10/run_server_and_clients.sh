#!/bin/bash

sleep .3
gnome-terminal -e "python3 ./ChatServer.py"

sleep .5
gnome-terminal -e "python3 ./ChatClient.py"

gnome-terminal -e "python3 ./ChatClient.py"


