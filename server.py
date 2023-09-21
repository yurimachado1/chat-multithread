import socket
import select
import sys
import threading
from collections import deque

# Lista de clientes conectados
client_list = []

# Lista das últimas mensagens
last_messages = deque(maxlen=15)

# Função para enviar uma mensagem para todos os clientes conectados
def broadcast_message(message, sender_socket):
    for client_socket in client_list:
        # Não envie a mensagem de volta para o remetente original
        if client_socket != sender_socket:
            try:
                client_socket.send(message.encode("utf-8"))
            except Exception as e:
                print("Erro ao enviar mensagem para o cliente:", e)
                client_socket.close()
                client_list.remove(client_socket)

# Função para lidar com as mensagens de um cliente
def handle_client(client_socket, addr):
    try:
        while True:
            message = client_socket.recv(2048).decode("utf-8")
            if not message:
                # Cliente desconectado
                client_socket.close()
                client_list.remove(client_socket)
                print(f"Cliente {addr} desconectado.")
                break
            elif message.strip().lower() == "@sair":
                # Cliente solicitou saída
                client_socket.close()
                client_list.remove(client_socket)
                print(f"Cliente {addr} saiu do chat.")
                broadcast_message(f"Cliente {addr} saiu do chat.", client_socket)
                break
            elif message.strip().lower() == "@ordenar":
                send_ordered_messages(client_socket)
            elif message.strip().lower() == "@upload":
                receive_file(client_socket)
            else:
                # Exibir a mensagem no terminal do servidor no formato ":: MENSAGEM"
                print(f"::{message}")
                last_messages.append(f"::{message}")
                # Enviar a mensagem para todos os outros clientes
                broadcast_message(f"::{message}", client_socket)
    except Exception as e:
        print(f"Erro ao lidar com o cliente {addr}: {e}")
        client_socket.close()
        client_list.remove(client_socket)

# Função para ordenar e enviar as últimas mensagens para um cliente
def send_ordered_messages(client_socket):
    ordered_messages = list(last_messages)
    ordered_messages.reverse()
    ordered_messages = "\n".join(ordered_messages)
    client_socket.send(ordered_messages.encode("utf-8"))

# Função para receber um arquivo do cliente
def receive_file(client_socket):
    try:
        file_name = client_socket.recv(2048).decode("utf-8")
        with open(file_name, "wb") as file:
            while True:
                data = client_socket.recv(2048)
                if not data:
                    break
                file.write(data)
        print(f"Arquivo '{file_name}' recebido com sucesso.")
    except Exception as e:
        print(f"Erro ao receber arquivo do cliente: {e}")

# Defina o endereço IP do servidor e a porta manualmente
ip_address = '192.168.0.151'
port = 4040

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((ip_address, port))
    server.listen(5)
    print(f"Servidor escutando em {ip_address}:{port}")
except Exception as e:
    print("Erro ao iniciar o servidor:", e)
    sys.exit(1)  # Encerra o programa em caso de erro de inicialização

# Loop principal do servidor
while True:
    try:
        conn, addr = server.accept()
        print(f"Nova conexão de {addr}")

        # Adicione o cliente à lista de clientes
        client_list.append(conn)

        # Inicie uma nova thread para lidar com as mensagens do cliente
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.daemon = True  # Defina como daemon
        client_thread.start()
    except Exception as e:
        print("Erro na conexão:", e)
        continue
