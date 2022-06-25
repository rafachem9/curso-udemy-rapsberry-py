#Instalar la librería pip3 install Adafruit_DHT

import Adafruit_DHT as dht

sensor = dht.DHT11

continuar = True

while continuar:
    dato= input("Mostar valores de temperatura y humedad: ")
    if dato== "z":
        continuar = False
    else:
        h,t=dht.read_retry(sensor, 4)
        print("Temperatura: ", t, "Humedad: ", h)
        
print("Fin del programa")
  