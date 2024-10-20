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
            x_coord_hex = client_socket.recv(1024)
            print(f"Received X coordinate (hex): {binascii.hexlify(x_coord_hex)}")

            # Receive Y coordinate
            y_coord_hex = client_socket.recv(1024)
            print(f"Received Y coordinate (hex): {binascii.hexlify(y_coord_hex)}")

            # Convert hex to integers
            # x_coord = int(x_coord_hex, 16) ^ XOR_DECRYPT_KEY
            # y_coord = int(y_coord_hex, 16) ^ XOR_DECRYPT_KEY
            # print(f"Decoded and decrypted coordinates: ({x_coord}, {y_coord})")
            # client_socket.send("Coordinates received successfully".encode())

            # IV:   000002DD7753AF60  XX XX XX XX XX XX 00 00 08 00 00 00 00 00 00 00     .¶7\÷...........
            #       000002DD7753AF70  CF 82 87 9D 47 0A 80 A9 00 00 00 00 00 00 00 00     Ï...G..©........
            #
            # 000002DD7753AF60  88 B6 37 5C F7 7F 00 00 08 00 00 00 00 00 00 00     .¶7\÷...........
            # 000002DD7753AF70  CF 82 87 9D 47 0A 80 A9 00 00 00 00 00 00 00 00     Ï...G..©........
            # 000002DD7753AF80  88 B6 37 5C F7 7F 00 00 20 00 00 00 00 00 00 00     .¶7\÷... .......
            # 000002DD7753AF90  84 9B A5 42 8C 90 39 B4 ED B2 2B 81 C4 12 1C 65     ..¥B..9´í²+.Ä..e
            # 000002DD7753AFA0  1F 7A 9F 4C 54 D0 E6 9C 52 C5 E5 35 5D E7 B2 BE     .z.LTÐæ.RÅå5]ç²¾
            # 000002DD7753AFB0  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00     ................


            # Send to socket
            client_socket.send(binascii.unhexlify("a0d2eba817e38b03cd063227bd32e353880818893ab02378d7db3c71c5c725c6bba0934b5d5e2d3ca6fa89ffbb374c31"))
            client_socket.send(binascii.unhexlify("96a35eaf2a5e0b430021de361aa58f8015981ffd0d9824b50af23b5ccf16fa4e323483602d0754534d2e7a8aaf8174dcf272d54c31860f"))

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
