import socket

def run_client():
    host = 'localhost'
    port = 5000
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect((host, port))
        print(f"Conectado al servidor en {host}:{port}")
        print("Escribe 'DESCONEXION' para terminar la conexión")
        
        while True:
            message = input("Mensaje a enviar: ")
            
            if not message:
                print("El mensaje no puede estar vacío")
                continue
                
            client_socket.send(message.encode('utf-8'))
            
            if message.upper() == "DESCONEXION":
                print("Solicitando desconexión del servidor...")
                break
                
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Respuesta del servidor: {response}")
            
    except ConnectionRefusedError:
        print("No se pudo conectar al servidor. Asegúrate de que el servidor esté en ejecución.")
    except ConnectionResetError:
        print("El servidor cerró la conexión inesperadamente.")
    except KeyboardInterrupt:
        print("\nCliente detenido por el usuario")
    finally:
        client_socket.close()
        print("Conexión cerrada")

if __name__ == "__main__":
    run_client()
