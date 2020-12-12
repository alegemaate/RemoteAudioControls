"""Client for media key server."""
import socket
import sys


def main(ip_address, port, command):
    """Set up connection to server."""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((ip_address, port))
    except socket.error:
        print(f"Could not connect to server at ip {ip_address}")
        exit(1)

    client.send(command.encode())
    from_server = client.recv(4096)
    client.close()
    print(from_server.decode())


if len(sys.argv) != 3:
    print("Requires 2 arguments, a valid ip and a command")
else:
    main(sys.argv[1], 8080, sys.argv[2])
