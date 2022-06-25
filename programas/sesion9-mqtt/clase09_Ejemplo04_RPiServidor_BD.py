import paho.mqtt.client as mqtt
import struct
import mysql.connector as mysql

def conectado (cliente, userdata, flagas, rc):
    if rc == 0:
        print('Conectado OK')
        cliente.subscribe('demo')
    else:
        print('No conectado')

def receptor (cliente, userdata, mensaje):
    #Para imprimir una lista, se hace un loop
    datos = struct.unpack('ff', mensaje.payload)
    valores = [round(datos[0],2), round(datos[1],2)]
    cursor.execute(query, valores)
    db.commit()
    print(datos)
 
db = mysql.connect(host ='192.168.0.17', user='roger', passwd='1234', database='test')
cursor = db.cursor()
query = 'INSERT INTO prueba3 (v1,v2) VALUE (%s, %s)'
 
cliente = mqtt.Client()
cliente.connect('192.168.0.17', 1883)

cliente.on_connect = conectado
cliente.on_message = receptor

cliente.loop_forever()
print('Fin del programa')