import socket
import threading
import time


def theater_joke(conn, seat_count):
    # Bilheteria
    time.sleep(2)
    conn.send(b"Voce entrou no teatro! Sente-se que a piada vai comecar\n")
    time.sleep(3)
    
    print(f"seat count 3: {seat_count}")
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
        print(f"seat count 4 {seat_count}")
        seat_count = seat_count - 1
        print(f"seat count 5 {seat_count}")
        conn.close()

def main(seat_count, max_seat):
    # Configurando o servidor
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 8085))
    server.listen()
    
    print(f"seat count 1: {seat_count}")
    while True:
        conn, addr = server.accept()
        print(f"Conectado a {addr}")

        conn.send(b"Gostaria de ouvir nosso show de uma piada so?\n")
        box_response = conn.recv(1024)

        if box_response.strip().lower() == b"sim":
            conn.send(b"Por favor aguarde que logo sera chamado\n")

            print(f"assentos ocupados: {seat_count}; maximo de assentos: {max_seat}")
            if seat_count <= max_seat:
                seat_count = seat_count + 1
                # Iniciando uma thread para lidar com o cliente
                print(f"seat count 2: {seat_count}")
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