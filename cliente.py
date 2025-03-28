import socket

# 1. Configuración del cliente
HOST = "127.0.0.1"  # Dirección IP del servidor
PORT = 12345        # Puerto del servidor

# 2. Crear el socket TCP del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3. Conectarse al servidor
client_socket.connect((HOST, PORT))
print(f"Conectado al servidor en {HOST}:{PORT}")

# 4. Enviar un mensaje al servidor
message = "Hola, servidor. Soy el cliente."
client_socket.sendall(message.encode("utf-8"))

# 5. Recibir respuesta del servidor
response = client_socket.recv(1024).decode("utf-8")
print(f"Servidor responde: {response}")

# 6. Cerrar la conexión
client_socket.close()
print("Conexión cerrada")
