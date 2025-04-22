# Client-Server-Communication-Application

This project is a Python-based socket programming assignment for client-server communication. It demonstrates a functional client-server communication model using TCP sockets, with support for multi-threaded client handling, status reporting, and basic file transfer operations.

🚀 Features:

- Real-time client-server communication via command-line interface (CLI)

- Unique client name assignment (Client01, Client02, etc.)

- Server-side session tracking with in-memory caching of client connection details

- Support for multiple concurrent client connections (up to 3)

Commands:

- status – request list of currently connected clients

- exit – disconnect from the server gracefully

- list – request list of available server-side files

- <filename> – request file transfer from server

- Message echoing with "ACK" confirmation from the server

🛠️ Technologies Used:

- Python 3

- Socket library

- Threading module for concurrent client handling

📚 Learning Highlights:

- Gained practical experience with TCP/IP socket programming

- Built a scalable and responsive server using multithreading

- Developed key insights into client connection management, message protocol design, and file transfer over networks
