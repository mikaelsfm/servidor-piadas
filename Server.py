import socket
import threading
import time

def box_office(conn):
    # Bilheteria
    conn.send(b"Gostaria de ouvir nosso show de uma piada so?\n")
    box_response = conn.recv(1024)
    
    if box_response.strip().lower() == b"sim":
        conn.send(b"Por favor aguarde que logo sera chamado")
        return
    

def theater_joke(conn):
    global seat_count
    seat_count += 1
    conn.send(b"Voce entrou no teatro! Sente-se que a piada vai comecar\n")
    time.sleep(5)
        
    # Piada de Knock Knock
    conn.send(b"Knock knock!\n")
    joke_response = conn.recv(1024)
    
    if joke_response.strip().lower() == b"who's there?":
        conn.send(b"Art\n")
        joke_response = conn.recv(1024)
        
        if joke_response.strip().lower() == b"art who?":
            conn.send(b"R2-D2!\n")
            time.sleep(2)
            conn.send(b"Obrigado e volte sempre!")
    seat_count -= 1
    conn.close()

def main():
    # Configurando o servidor
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 8085))
    server.listen()
    
    seat_count = 0
    max_seat = 2
    
    while True:
        
        conn, addr = server.accept()

        get_ticket = threading.Thread(target=box_office, args=(conn,))
        get_ticket.start()
        
        if seat_count <= max_seat:
            # Iniciando uma thread para lidar com o cliente
            client_handler = threading.Thread(target=theater_joke, args=(conn,))
            client_handler.start()

main()
