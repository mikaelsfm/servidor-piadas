import socket
import threading

def handle_client(client_socket):
    # # Bilheteria
    # client_socket.send(b"Bem-vindo a bilheteria do teatro!\n")
    
    # # Fila de espera
    # client_socket.send(b"Voce esta na fila de espera...\n")
    
    # # Entrando no teatro
    # client_socket.send(b"Voce entrou no teatro!\n")
    
    # Piada de Knock Knock
    client_socket.send(b"Knock knock!\n")
    response = client_socket.recv(1024)
    
    if response.strip().lower() == b"who's there?":
        client_socket.send(b"Art.\n")
        response = client_socket.recv(1024)
        
        if response.strip().lower() == b"art who?":
            client_socket.send(b"R2-D2\n")
            
        else:
            client_socket.send(b"Desculpe, eu me perdi na piada, vamos de novo?\n")
    else:
        client_socket.send(b"Desculpe, eu me perdi na piada!\n")
    
    client_socket.close()

def main():
    # Configurando o servidor
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 8085))
    server.listen(5)
    
    while True:
        client_socket, addr = server.accept()
        print(f"Cliente {addr[0]}:{addr[1]}")
        
        # Iniciando uma thread para lidar com o cliente
        client_handler = threading.Thread(target=handle_client, args=(client_socket))
        client_handler.start()

if __name__ == "__main__":
    main()
