import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

def conectado(cliente,userdata,flags,rc):
    if rc == 0:
        print("Cliente conectado OK")
        cliente.subscribe("demo")
    else:
        print("Cliente no se pudo conectar")
def receptor(cliente,userdata,mensaje):
    men = mensaje.payload.decode()
    print(men)
    if men == "a":
        GPIO.output(2,GPIO.HIGH)
    elif men == "b":
        GPIO.output(2,GPIO.LOW)

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
cliente = mqtt.Client()
cliente.connect("192.168.1.7",1883)

cliente.on_connect = conectado
cliente.on_message = receptor

cliente.loop_forever()
print("Fin de programa")