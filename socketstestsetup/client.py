import socket
import threading

HOST = "35.179.138.206"
PORT = 5050

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Message from server: {message}\nEnter a message: \n")
        except:
            print("Connection closed by the server.")
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print("Connected to the server!")

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    try:
        while True:
            message = input("Enter a message: \n")
            client_socket.sendall(message.encode('utf-8'))
    except KeyboardInterrupt:
        print("Disconnecting...")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
