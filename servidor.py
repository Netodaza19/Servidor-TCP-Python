import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Conexión establecida con {client_address}")
    
    try:
        while True:
            # Datos del cliente
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            
            print(f"Mensaje recibido de {client_address}: {data}")
            
            if data.upper() == "DESCONEXION":
                print(f"Solicitud de desconexión recibida de {client_address}")
                client_socket.send("Conexión cerrada por solicitud del cliente".encode('utf-8'))
                break
            else:
                # Instrucción para responder en mayúsculas
                response = data.upper()
                client_socket.send(response.encode('utf-8'))
                
    except ConnectionResetError:
        print(f"Cliente {client_address} cerró la conexión inesperadamente")
    finally:
        client_socket.close()
        print(f"Conexión con {client_address} cerrada")

def start_server():
    host = 'localhost'
    port = 5000
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Servidor TCP iniciado en {host}:{port}. Esperando conexiones...")
    
    try:
        while True:
            client_socket, client_address = server_socket.accept()
            client_thread = threading.Thread(
                target=handle_client,
                args=(client_socket, client_address)
            )
            client_thread.start()
    except KeyboardInterrupt:
        print("\nServidor detenido por el usuario")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()
