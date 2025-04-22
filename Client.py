"""
Client.py
"""

import socket
import threading
from datetime import datetime

# Client.py
import socket

HOST = "127.0.0.1"
PORT = 65432


def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    client_name = client.recv(1024).decode("utf-8")
    # if server is full, deploy message
    print(f"{client_name}")

    while True:
        message = input("Enter message: ")
        client.send(message.encode("utf-8"))
        if message.lower() == "exit":
            break
        response = client.recv(1024).decode("utf-8")
        print(f"Server: {response}")

    client.close()


if __name__ == "__main__":
    start_client()
