import socket
import threading


HOST = "0.0.0.0" 
PORT = 5050


clients = []
messages = []  
messages_lock = threading.Lock()

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket: 
            try:
                client.sendall(message.encode('utf-8'))
            except:
                clients.remove(client)  

def handle_client(client_socket):
    while True:
        try:
          
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break  

            with messages_lock:
                messages.append(message)

            broadcast(message, client_socket)
        except:
            break

    clients.remove(client_socket)
    client_socket.close()
    print("Client disconnected")

def start_server():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((HOST, PORT))
        server_socket.listen(2) 
        print(f"Server started on {HOST}:{PORT}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"New connection from {client_address}")
            clients.append(client_socket)

            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()
    except KeyboardInterrupt:
        print("\nShutting down the server...")
    finally:
        for client in clients:
            client.close()
        if server_socket:
            server_socket.close()
        print("Server closed.")


if __name__ == "__main__":
    start_server()
