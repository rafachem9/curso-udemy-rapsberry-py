from bluedot.btcomm import BluetoothServer

def leer(data):
    print(data)

print("Iniciando servidor bluetooth")
s=BluetoothServer(leer)