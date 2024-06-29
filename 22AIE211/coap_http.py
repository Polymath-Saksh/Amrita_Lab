import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set the server address and port
server_address = ('localhost', 5683)

# Bind the socket to the server address
sock.bind(server_address)

while True:
    print('Waiting for incoming CoAP requests...')

    # Receive a CoAP request
    data, address = sock.recvfrom(1024)

    # Process the CoAP request
    # ...

    # Send a CoAP response
    response = b'CoAP response'
    sock.sendto(response, address)