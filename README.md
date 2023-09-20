# Chat em Python com Múltiplos Usuários

Este é um programa de chat simples em Python que permite múltiplos usuários conversarem em um servidor. Ele oferece recursos como formatação de mensagens, comandos para ordenar mensagens, fazer logout, fazer upload e download de arquivos.

## Funcionalidades

- **Múltiplos Usuários:** Vários clientes podem se conectar e conversar simultaneamente.

- **Formatação de Mensagens:** As mensagens são impressas no formato ":: MENSAGEM".

- **Comandos Suportados:**
    - `@SAIR`: Faz logout do cliente.
    - `@UPLOAD`: Faz upload de um arquivo para o servidor.
    - `@DOWNLOAD`: Faz download de um arquivo do servidor.
    - `@ORDENAR`: Mostra as últimas 15 mensagens, ordenadas pelo horário de envio.

## Como Usar

### Executando o Servidor

1. Execute o servidor com o seguinte comando:

   ```bash
   python server.py PORTA
Substitua PORTA pela porta em que deseja que o servidor escute (por padrão, é 19000).

Executando o Cliente
Execute um cliente com o seguinte comando:

bash
Copy code
python client.py ENDEREÇO_DO_SERVIDOR PORTA
Substitua ENDEREÇO_DO_SERVIDOR pelo endereço IP do servidor (por exemplo, 127.0.0.1) e PORTA pela mesma porta que você configurou no servidor.



Comandos do Cliente
Para enviar mensagens, basta digitá-las e pressionar Enter.
Use @SAIR para sair do chat.
Use @UPLOAD NOME_DO_ARQUIVO para fazer upload de um arquivo.
Use @DOWNLOAD NOME_DO_ARQUIVO para fazer download de um arquivo.
Use @ORDENAR para ver as últimas 15 mensagens ordenadas por horário.
