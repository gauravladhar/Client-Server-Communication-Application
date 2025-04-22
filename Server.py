"""
-------------------------------------------------------
Server.py listens to the client connections. When a new
client connects, the server accepts the connection and
reads any data.
-------------------------------------------------------
"""
# Server.py
import socket
import threading
import datetime

# Server configuration
HOST = "127.0.0.1"
PORT = 65432

# Define max clients
MAX_CLIENTS = 3

# Maintain a cache of connected clients
clients = {}
client_counter = 1
lock = threading.Lock()


def handle_client(connection, address, client_name):
    global clients
    with lock:
        # get datetime of connection
        clients[client_name] = {
            "connected_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "disconnected_at": None
        }

    # print client details
    print(f"{client_name} connected from {address}")

    # get data
    try:
        while True:
            data = connection.recv(1024).decode("utf-8")
            if not data:
                break
            # print data to server from given client
            print(f"Received from {client_name}: {data}")

            if data.lower() == "status":
                connection.send(str(clients).encode("utf-8"))
            # if client disconnects, exit
            elif data.lower() == "exit":
                break
            # send data ACK to client
            else:
                connection.send(f"{data} ACK".encode("utf-8"))
    finally:
        with lock:
            # get datetime of disconnection
            clients[client_name]["disconnected_at"] = datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S")
            # remove client from directory
            del clients[client_name]
        print(f"{client_name} disconnected")
        # close connection
        connection.close()


def start_server():
    global client_counter
    # create new socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # allow reuse of the same address to prevent "address already in use" errors
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST, PORT))
    server.listen(MAX_CLIENTS)
    # print message acknowledging connection from HOST and PORT
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        connection, address = server.accept()
        with lock:
            # if the server is full (clients > 3)
            if len(clients) >= MAX_CLIENTS:
                connection.send(
                    "Server is full. Try again later.".encode("utf-8"))
                # close connection
                connection.close()
                continue

            # set client name
            client_name = f"Client{client_counter:02d}"
            # increment counter (client + XX)
            client_counter += 1

        connection.send(client_name.encode("utf-8"))
        threading.Thread(target=handle_client, args=(
            connection, address, client_name), daemon=True).start()


if __name__ == "__main__":
    start_server()
