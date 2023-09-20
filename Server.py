import socket
import threading
import time


def theater_joke(conn, seat_count):
    # Bilheteria
    time.sleep(2)
    conn.send(b"Voce entrou no teatro! Sente-se que a piada vai comecar\n")
    time.sleep(3)
    
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
        seat_count = seat_count - 1
        conn.close()

def main(seat_count, max_seat):
    # Configurando o servidor
    server = socket.socket()
    server.bind(("127.0.0.1", 8085))
    server.listen()

    while True:
        
        conn, addr = server.accept()

        conn.send(b"Gostaria de ouvir nosso show de uma piada so?\n")
        box_response = conn.recv(1024)

        if box_response.strip().lower() == b"sim":
            conn.send(b"Por favor aguarde que logo sera chamado\n")

            if seat_count <= max_seat:
                seat_count = seat_count + 1
                # Iniciando uma thread para lidar com o cliente
                client_handler = threading.Thread(target=theater_joke, args=(conn, seat_count))
                client_handler.start()
            
            else:
                while seat_count <= max_seat:
                    client_handler = threading.Thread(target=theater_joke, args=(conn, seat_count))
                    client_handler.start()


if __name__ == '__main__':
    max_seat = 2
    seat_count = 0
    main(seat_count, max_seat)