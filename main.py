import socket
from datetime import datetime
import time
import os
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 9999))
server.listen()


start_time = time.time()
connected_clients = 0

facts = [
    "Did you know? The first computer virus was created in 1986.",
    "Fact: The internet is over 30 years old.",
    "Random: Python is named after Monty Python, not the snake!",
]

while True:
    client, addr = server.accept()
    connected_clients += 1
    uptime = time.time() - start_time
    print(f"Connection from {addr}")

    # Welcome message with system info
    client.send(f"You are connected to the server at {datetime.now().strftime('%H:%M:%S')}!\n".encode())
    client.send(f"Server uptime: {int(uptime)} seconds.\n".encode())
    client.send(f"Total clients connected so far: {connected_clients}\n".encode())

    # Send a random fact
    client.send(f"Random Fact: {random.choice(facts)}\n".encode())

    time.sleep(2)

    # Additional messages
    client.send("The server time updates every 2 seconds.\n".encode())
    for i in range(3):
        client.send(f"Server ping {i + 1}: {datetime.now().strftime('%H:%M:%S')}\n".encode())
        time.sleep(2)

    # Goodbye message
    client.send("You are being disconnected! Thanks for connecting.\n".encode())
    client.close()