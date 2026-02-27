import socket
import threading


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind(("0.0.0.0", 12345))


server.listen()
print("Server started and listening...")

clients = []
usernames = []



def broadcast(message):
    for client in clients:
        client.send(message)



def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            username = usernames[index]
            usernames.remove(username)
            broadcast(f"{username} left the chat".encode())
            client.close()
            break



def receive():
    while True:
        client, address = server.accept()
        print("Connected with", address)

        
        client.send(b"Send Username")
        username = client.recv(1024).decode()

        clients.append(client)
        usernames.append(username)

        print(username, "joined the chat")
        broadcast(f"{username} joined the chat".encode())

        # Start thread for this client
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


receive()