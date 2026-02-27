import socket
import threading


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_ip = input("Enter server IP: ")
client.connect((server_ip, 12345))



def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == "Send Username":
                username = input("Enter your username: ")
                client.send(username.encode())
            else:
                print(message)
        except:
            print("Connection closed")
            client.close()
            break



def send_messages():
    while True:
        message = input()
        client.send(message.encode())



t1 = threading.Thread(target=receive_messages)
t2 = threading.Thread(target=send_messages)


t1.start()
t2.start()

t1.join()
t2.join()