import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 7777))
s.listen(1)

print("Servidor de Chat \n")

while True:
    print("Esperando conexion del cliente...")
    sc, addr = s.accept()
    print("Cliente conectado desde:", addr)

    while True:
        recibido = sc.recv(1024)
        if recibido.decode('utf-8') == "quit":
            break
        print("Recibido", recibido)

        nuestra_respuesta = "Hola cliente, yo soy el servidor"
        sc.send(nuestra_respuesta.encode('utf-8'))

print("Adios")
sc.close()
s.close()
