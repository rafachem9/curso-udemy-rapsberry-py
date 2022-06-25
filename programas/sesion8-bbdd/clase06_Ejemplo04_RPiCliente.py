import mysql.connector as mysql
import socket

#Conexión a la BD
db= mysql.connect(host="192.168.1.25", user="roger", passwd="1234",database="test")
cursor = db.cursor()

#Abrimos el socket
s =socket.socket()
s.bind(("192.168.1.25", 2020))
s.listen(10)

#Definición de los valores que se añadirán a la BD
query = "INSERT INTO prueba2 (v1,v2,v3) VALUES (%s, %s, %s)"



#Da la información del cliente, y espera por datos
print("Esperando conexiones")
while True:
    (sc, addrc) = s.accept()
    print("Cliente conectado", addrc)
    continuar= True
    while continuar:
        data =sc.recv(64)
        if not data:
            continuar= False
            print("Cliente desconectado")
        else:
            print(data)
            valores= (data[0],data[1],data[2])
            cursor.execute(query, valores)
            db.commit()
            
#Cerrar cursor y DB
cursor.close()
db.close()
#Cerrar Socket
s.close()

print("Fin de programa")
