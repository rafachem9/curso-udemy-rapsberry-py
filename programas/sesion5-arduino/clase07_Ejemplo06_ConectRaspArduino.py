import serial

s=serial.Serial("/dev/ttyACM0",9600)

try:
    while True:
        temperatura = s.readline()
        nivelLuz = s.readline()
        #decode es para pasar a string
        temp, luz= (temperatura.decode(), nivelLuz.decode())
        print(temp, luz)
        
except:
    s.close()
    print("Fin del Programa")