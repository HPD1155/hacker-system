import socket
import os
import requests
import sys
import urllib
import time
from datetime import datetime
from urllib import request as rq

def logger():
    s = socket.socket()
    win_ip = input("ip> ")

    try:
        host = win_ip
        port = 22

        s.bind((host, 22))
    except:
        print("(Alert): Address is already in use!")
        print("(Alert): Try different address")
        time.sleep(2)

    while True:
        try:
            s.listen(5)
            conn, address = s.accept()

            print("[log]: IP found: " + str(address[0]))

        except:
            pass
            logger()

logger()