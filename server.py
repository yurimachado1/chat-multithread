import socket
import select
import sys
import threading
from collections import deque


client_list = []


last_messages = deque(maxlen=15)


def broadcast_message(message, sender_socket):
    for client_socket in client_list:
        
        if client_socket != sender_socket:
            try:
                client_socket.send(message.encode("utf-8"))
            except Exception as e:
                print("Erro ao enviar mensagem para o cliente:", e)
                client_socket.close()
                client_list.remove(client_socket)


def handle_client(client_socket, addr):
    try:
        while True:
            message = client_socket.recv(2048).decode("utf-8")
            if not message:
                
                client_socket.close()
                client_list.remove(client_socket)
                print(f"Cliente {addr} desconectado.")
                break
            elif message.strip().lower() == "@sair":
               
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
                
                print(f"::{message}")
                last_messages.append(f"::{message}")
               
                broadcast_message(f"::{message}", client_socket)
    except Exception as e:
        print(f"Erro ao lidar com o cliente {addr}: {e}")
        client_socket.close()
        client_list.remove(client_socket)


def send_ordered_messages(client_socket):
    ordered_messages = list(last_messages)
    ordered_messages.reverse()
    ordered_messages = "\n".join(ordered_messages)
    client_socket.send(ordered_messages.encode("utf-8"))


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
    sys.exit(1)  


while True:
    try:
        conn, addr = server.accept()
        print(f"Nova conexão de {addr}")

       
        client_list.append(conn)

        
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.daemon = True  
        client_thread.start()
    except Exception as e:
        print("Erro na conexão:", e)
        continue
