import socket
import threading as th

def manejar(sc,addrc):
    print("Cliente conectado: ", addrc)
    continuar = True
    while continuar:
        data = sc.recv(64)
        if not data:
            continuar = False
            print("Cliente desconectado",addrc)
        else:
            print(data)
    sc.close()

s=socket.socket()
s.connect(("192.168.1.25",2020))
print("servidor conectado")
s.listen(10)
print("Esperando conexion...")

while True:
    (sc,addrc) = s.accept()
    hilo = th.Thread(target = manejar, args=(sc,addrc))
    hilo.start()
    
print("Fin de programa")
sc.close()