import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

while True:
    # Wait for a connection
    print('Waiting for a connection...')
    client_socket, client_address = server_socket.accept()
    print('Connected to:', client_address)

    try:
        while True:
            # Receive data from the client
            data = client_socket.recv(1024)
            if data:
                # Process the received data
                print('Received:', data.decode())

                # Send a response back to the client
                response = 'Hello from the server!'
                client_socket.sendall(response.encode())
            else:
                # No more data from the client
                print('Connection closed by client.')
                break

    finally:
        # Clean up the connection
        client_socket.close()