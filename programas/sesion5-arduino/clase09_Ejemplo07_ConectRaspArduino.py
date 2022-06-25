import serial

s=serial.Serial("/dev/ttyACM0",9600)

continuar = True
while continuar:
    dato= input("Ponga una letra: ")
    if dato == "z":
        continuar = False
    else:
        #encode convierte de string a byte
        s.write(dato.encode())        

s.close()
print("Fin del Programa")