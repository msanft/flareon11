import socket, binascii

HOST = "192.168.56.103"
PORT = 31337

XOR_DECRYPT_KEY = int("133713371337133713371337133713371337133713371337133713371337133713371337133713371337133713371337", 16)

def start_server(host='localhost', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address}")

        try:
            # Receive X coordinate
            x_coord_hex = client_socket.recv(1024).decode().strip()
            print(f"Received X coordinate (hex): {x_coord_hex}")

            # Receive Y coordinate
            y_coord_hex = client_socket.recv(1024).decode().strip()
            print(f"Received Y coordinate (hex): {y_coord_hex}")

            # Convert hex to integers
            x_coord = int(x_coord_hex, 16) ^ XOR_DECRYPT_KEY
            y_coord = int(y_coord_hex, 16) ^ XOR_DECRYPT_KEY
            print(f"Decoded and decrypted coordinates: ({x_coord}, {y_coord})")
            client_socket.send("Coordinates received successfully".encode())

        except Exception as e:
            print(f"Error: {e}")
        finally:
            client_socket.close()

try:
    start_server(HOST, PORT)
except KeyboardInterrupt:
    print("\nServer stopped.")
except Exception as e:
    print(f"An error occurred: {e}")
