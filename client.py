import socket
import select
import sys
import threading

if len(sys.argv) < 2:
    print("usage: client SERVER_IP [PORT]")
    sys.exit(1)

ip_address = sys.argv[1]
port = int(sys.argv[2]) if len(sys.argv) > 2 else 19000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((ip_address, port))

running = True

# Função para receber mensagens do servidor e imprimir
def receive_messages():
    while running:
        try:
            message = server.recv(2048).decode("utf-8")
            print(message)
        except:
            continue

# Inicia uma thread para receber mensagens do servidor
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while running:
    message = input()
    server.send(message.encode("utf-8"))

server.close()
