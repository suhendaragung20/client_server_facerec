import socket
import cv2
import random
import _thread

host = "10.14.6.163"  # e.g. localhost, 192.168.1.123.

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client_socket.connect((host, 5005))

print("Connected to Server")

while True:
    a = 1
