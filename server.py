import socket
import select
import sys
import threading
import os

# Lista para armazenar as mensagens
messages = []

# Lista para armazenar os arquivos no servidor
server_files = {}

# Função para enviar mensagens para todos os clientes
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                client.close()
                remove(client)

# Função para remover um cliente desconectado
def remove(client):
    if client in clients:
        clients.remove(client)

# Função para ordenar e mostrar as últimas 15 mensagens
def send_recent_messages(client_socket):
    recent_messages = messages[-15:]
    for message in recent_messages:
        client_socket.send(message.encode("utf-8"))

# Função para fazer upload de um arquivo para o servidor
def upload_file(client_socket, file_name):
    file_data = client_socket.recv(1024)
    with open(file_name, "wb") as file:
        while file_data:
            file.write(file_data)
            file_data = client_socket.recv(1024)
    server_files[file_name] = True

# Função para fazer download de um arquivo do servidor
def download_file(client_socket, file_name):
    if file_name in server_files:
        with open(file_name, "rb") as file:
            file_data = file.read(1024)
            while file_data:
                client_socket.send(file_data)
                file_data = file.read(1024)
    else:
        client_socket.send("Arquivo não encontrado no servidor.".encode("utf-8"))

# Configuração do servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

port = int(sys.argv[1]) if len(sys.argv) > 1 else 19000
server.bind(('0.0.0.0', port))
server.listen(5)

# Lista de clientes conectados
clients = []

print("Servidor de chat está ativo na porta", port)

# Função para lidar com as mensagens dos clientes
def client_thread(client_socket):
    client_socket.send("Bem-vindo ao chat. Use @SAIR para sair.\n".encode())

    while True:
        try:
            message = client_socket.recv(2048).decode("utf-8")
            if message:
                if message == "@SAIR":
                    remove(client_socket)
                    client_socket.close()
                elif message.startswith("@UPLOAD"):
                    _, file_name = message.split()
                    upload_file(client_socket, file_name)
                elif message.startswith("@DOWNLOAD"):
                    _, file_name = message.split()
                    download_file(client_socket, file_name)
                elif message == "@ORDENAR":
                    send_recent_messages(client_socket)
                else:
                    message_to_broadcast = f"::{message}"
                    messages.append(message_to_broadcast)
                    if len(messages) > 15:
                        messages.pop(0)
                    broadcast(message_to_broadcast.encode(), client_socket)
            else:
                remove(client_socket)
                client_socket.close()
        except Exception as e:
            print("Erro:", e)
            continue

# Loop principal do servidor
while True:
    client_socket, addr = server.accept()
    clients.append(client_socket)
    print(addr[0] + " conectou-se ao servidor")

    # Inicia uma nova thread para lidar com o cliente
    client_thread_handler = threading.Thread(target=client_thread, args=(client_socket,))
    client_thread_handler.start()