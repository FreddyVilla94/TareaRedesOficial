# Programa Servidor

#Importacines:
import socket #utilidades de red y conexion
import index
#Definimos parámetros necesarios por defecto
ip = index.getHostIp()
puerto = 9797
dataConection = (ip, puerto)
conexionesMaximas = 20 #Podrán conectarse 5 clientes como máximo

#Creamos el servidor.
#socket.AF_INET para indicar que utilizaremos Ipv4
#socket.SOCK_STREAM para utilizar TCP/IP (no udp)
socketServidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socketServidor.bind(dataConection)          #Asignamos los valores del servidor
socketServidor.listen(conexionesMaximas)    #Asignamos el número máximo de conexiones

print("Esperando conexiones en %s:%s" %(ip, puerto))
cliente, direccion = socketServidor.accept()
print("Conexion establecida con %s:%s" %(direccion[0], direccion[1]))

#Bucle de escucha. En él indicamos la forma de actuar al recibir las tramas del cliente
while True:
    datos = cliente.recv(1024) #El número indica el número maximo de bytes
    if datos == "exit":
        cliente.send("exit".encode('utf-8'))
        break
    print("RECIBIDO: %s" %datos)
    cliente.sendall("-- Recibido --".encode('utf-8'))

print("------- CONEXIÓN CERRADA ---------")
socketServidor.close()