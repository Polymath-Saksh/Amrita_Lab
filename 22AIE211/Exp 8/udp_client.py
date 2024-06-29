import socket

def main():
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set the server address and port
    server_address = ('localhost', 12345)

    try:
        # Send data to the server
        message = 'Hello, server!'
        client_socket.sendto(message.encode(), server_address)

        # Receive response from the server
        data, server = client_socket.recvfrom(1024)
        print('Received:', data.decode())

    finally:
        # Close the socket
        client_socket.close()

if __name__ == '__main__':
    main()