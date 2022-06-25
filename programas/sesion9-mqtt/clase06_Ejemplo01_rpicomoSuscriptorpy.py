import paho.mqtt.client as mqtt

def conectado(cliente, userdata, flags, rc):
    if rc == 0:
        print ('Cliente conectado OK')
        cliente.subscribe('demo')
    else:
        print ('El cliente no se pudo conectar')
        
def receptor (cliente, userdata, mensaje):
    print(mensaje.payload)
    

#Creamos el objeto cliente
cliente = mqtt.Client('Rafa')
cliente.connect ('192.168.0.17', 1883)

cliente.on_connect = conectado
cliente.on_message = receptor

cliente.loop_forever()
print('Fin del programa')