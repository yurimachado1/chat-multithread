# Chat multi-thread
Trabalho desenvolvido por Cleber Trindade e Yuri Machado. Este é um sistema de chat em Python que se baseia em um ambiente multi-thread, com um servidor e cliente. O servidor é capaz de receber várias conexões de clientes e permite que eles se comuniquem entre si. Além disso, o sistema suporta algumas funcionalidades especiais, como a exibição das últimas 15 mensagens ordenadas pelo horário de envio, logout do cliente, upload e download de arquivos.

## Requisitos
Para executar o sistema de chat, você precisa de:

Python 3.x instalado no seu sistema.
## Instruções de Uso
### Servidor
Abra um terminal e navegue até o diretório onde o arquivo do servidor está localizado.

Execute o servidor Python com o seguinte comando:
    
    python server.py
    
Substitua ***server.py*** pelo nome do arquivo do servidor, se for diferente.

O servidor estará agora escutando por conexões de clientes na porta especificada (no código fornecido, a porta padrão é 4040). Você verá uma mensagem indicando que o servidor está pronto para aceitar conexões.

### Cliente
Abra um terminal e navegue até o diretório onde o arquivo do cliente está localizado.

Execute o cliente Python com o seguinte comando:

    python client.py
Substitua ***client.py*** pelo nome do arquivo do cliente, se for diferente.

### Funcionalidades disponíveis

O cliente solicitará que você insira uma mensagem. Digite sua mensagem e pressione Enter para enviá-la ao servidor. Você verá suas mensagens sendo exibidas no terminal.

#### Sair do chat: 
Para sair do chat, digite "@SAIR" e pressione Enter. Isso encerrará a conexão do cliente com o servidor e fechará o cliente.

#### Ordenar mensagens
Para exibir as últimas 15 mensagens ordenadas pelo horário de envio, digite "@ORDENAR" e pressione Enter.

#### Upload
Para fazer upload de um arquivo para o servidor, digite "@UPLOAD" e pressione Enter. Você será solicitado a inserir o nome do arquivo a ser enviado. Certifique-se de que o arquivo esteja no mesmo diretório que o cliente Python.

#### Download
Para fazer download de um arquivo do servidor, digite "@DOWNLOAD" e pressione Enter. Você será solicitado a inserir o nome do arquivo a ser baixado. O arquivo será salvo no mesmo diretório que o cliente Python.

## Exemplos de Uso

### Enviando Mensagens
Cliente:


    Digite sua mensagem: Olá, pessoal!
Servidor:


    Nova conexão de ('192.168.0.100', 12345)
    ::Cliente 192.168.0.100: Olá, pessoal!

### Saindo do Chat

Cliente:
    
    Digite sua mensagem: @SAIR

Servidor:
    
    Cliente 192.168.0.100 saiu do chat.

### Exibindo Mensagens Ordenadas

Cliente:


    Digite sua mensagem: @ORDENAR

Servidor:


    ::Mensagem 15
    ::Mensagem 14
    ::Mensagem 13
    ::Mensagem 12
    ::Mensagem 11
    ::Mensagem 10
    ::Mensagem 9
    ::Mensagem 8
    ::Mensagem 7
    ::Mensagem 6
    ::Mensagem 5
    ::Mensagem 4
    ::Mensagem 3
    ::Mensagem 2
    ::Mensagem 1

### Enviando Arquivos para o Servidor
Cliente:

    Digite sua mensagem: @UPLOAD
    Nome do arquivo a ser enviado: arquivo.txt

Servidor:

    Arquivo 'arquivo.txt' recebido com sucesso.

### Baixando Arquivos do Servidor
Cliente:

    Digite sua mensagem: @DOWNLOAD
    Nome do arquivo a ser baixado: arquivo.txt

Servidor:

    Cliente 192.168.0.100 solicitou o download do arquivo 'arquivo.txt'.

Isso resume como usar o sistema de chat em Python. Você pode executar vários clientes em diferentes terminais para iniciar conversas simultâneas. Certifique-se de que o servidor esteja em execução antes de iniciar os clientes.
