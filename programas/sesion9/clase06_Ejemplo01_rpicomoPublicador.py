import paho.mqtt.client as mqtt
import random
import time

#Creamos el objeto cliente
cliente = mqtt.Client('Rafa')
cliente.connect ('192.168.0.17', 1883)

#Envía string y números. No puede enviar listas

for i in range(50):
    data = random.randint(0,100)
    cliente.publish('demo',data)
    time.sleep(2)

print('Fin del programa')