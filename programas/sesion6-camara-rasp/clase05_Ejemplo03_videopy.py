import picamera

cm = picamera.PiCamera()
#Cambio de resolución
cm.resolution= (620,480)
#Introducir texto en el video
cm.annotate_text= ("Demo de camara")
#Rotar la camara 
cm.rotation = 180

print("Iniciando grabación video")

#Elige la carpeta donde se guarda y nombre del archivo
cm.start_recording("/home/pi/demo.h264")
#Tiempo de grabación
cm.wait_recording(10)
cm.stop_recording()
print("Fin del programa")