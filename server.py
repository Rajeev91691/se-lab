import socket

HOST = '127.0.0.1'  # Localhost
PORT = 55  # Port to listen on

def handle_client(conn):
    """Handles the file request from the client."""
    try:
        filename = conn.recv(1024).decode().strip()  # Receive filename from client
        print(f"Client requested file: {filename}")

        # Open and read the file
        with open(filename, 'r') as file:
            data = file.read()

        # Send file data
        conn.sendall(data.encode())
    except FileNotFoundError:
        conn.sendall(b"ERROR: File not found")
    except Exception as e:
        conn.sendall(f"ERROR: {str(e)}".encode())
    finally:
        conn.close()

def main():
    """Starts the server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)  # Listen for a single connection
        print(f"Server listening on port {PORT}...")

        while True:
            conn, addr = server_socket.accept()
            print(f"Connected by {addr}")
            handle_client(conn)

if __name__ == "__main__":
    main()

