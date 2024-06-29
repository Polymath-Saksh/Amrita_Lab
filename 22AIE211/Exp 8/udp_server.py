import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific IP address and port
server_address = ('localhost', 12345)
sock.bind(server_address)

while True:
    print('Waiting for incoming data...')
    data, address = sock.recvfrom(1024)
    
    print(f'Received {len(data)} bytes from {address}')
    print(f'Data: {data.decode()}')
    
    # Process the received data here
    
    # Send a response back to the client
    response = 'Hello, client!'
    sock.sendto(response.encode(), address)