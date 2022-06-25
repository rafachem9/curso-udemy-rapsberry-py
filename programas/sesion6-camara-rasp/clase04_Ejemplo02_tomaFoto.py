import picamera

cm= picamera.PiCamera()
i=0

#Captura una imagen, y la guarda en la carpeta
continuar =True
while continuar:
    dato = input("Ponga una instrucción: ")
    if dato == "z":
        continuar = False
    else:
        print("Sacando la foto", i)
        cm.capture("/home/pi/test%01d.jpg"%i)
        i=i+1


print("Fin del programa")