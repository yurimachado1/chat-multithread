import socket
import sys
import threading


def user_input_thread():
    while True:
        message = input("Digite sua mensagem: ")
        server.send(message.encode("utf-8"))


ip_address = '192.168.0.151'
port = 4040

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip_address, port))
    print("Conexão com o servidor estabelecida com sucesso!")
except Exception as e:
    print("Erro ao conectar ao servidor:", e)
    sys.exit(1)  


user_input_thread = threading.Thread(target=user_input_thread)
user_input_thread.start()


while True:
    try:
        message = server.recv(2048).decode("utf-8")
        if not message:
            print("Servidor desconectado.")
            break
        print(message)
    except Exception as e:
        print("Erro ao receber mensagem do servidor:", e)
        break
