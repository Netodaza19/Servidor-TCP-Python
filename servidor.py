import socket

# 1. Configuración del servidor
HOST = "0.0.0.0"  # Escucha en todas las interfaces de red
PORT = 12345      # Puerto donde escuchará el servidor

# 2. Crear el socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))  # Enlazar a la IP y puerto
server_socket.listen(1)  # Escuchar solo 1 conexión a la vez

print(f"Servidor escuchando en {HOST}:{PORT}...")

while True:
    # 3. Aceptar conexión de un cliente
    client_socket, client_address = server_socket.accept()
    print(f"Conexión aceptada desde {client_address}")

    # 4. Recibir datos del cliente
    data = client_socket.recv(1024).decode("utf-8")
    print(f"Cliente dice: {data}")

    # 5. Enviar una respuesta al cliente
    response = "Mensaje recibido con éxito"
    client_socket.sendall(response.encode("utf-8"))

    # 6. Cerrar la conexión con el cliente
    client_socket.close()
    print("Conexión cerrada")

