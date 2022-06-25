import serial                         #Leer datos del monitor serial        
import time                           #Para retrasar el tiempo de lecturas
from datetime import date, datetime   #Indicar la hora y el día
import mysql.connector as mysql       #Base de datos

#Lectura del monitor serial de arduino
s=serial.Serial("/dev/ttyACM0",9600)
#Conexión a la BD

db= mysql.connect(host="192.168.1.25", user="roger", passwd="1234",database="datosArduino")
cursor = db.cursor()
#Insertar elementos
query="INSERT INTO sensores2(FechaActualizacion, Temperatura, Luminosidad) VALUES (NOW(),%s,%s)"
valores = (1,2)
try:
    while True:
        fechayHora=datetime.now()
        
        fecha=fechayHora.strftime("%d/%m/%Y")
        hora=fechayHora.strftime("%H:%M")
        
        #Lee los datos del Serial
        temperatura = s.readline()
        nivelLuz = s.readline()
        #decode es para pasar a string
        temp=temperatura.decode()
        luz=nivelLuz.decode()
        #Imprime los datos en pantalla
        print(fecha)
        print(hora) 
        print(f"temperatura {temp} ºC")
        print(f"Valor luminosidad: {luz}")
        
        valores= (temp, luz)
        cursor.execute(query, valores)
        db.commit()
        time.sleep(600)
        
        
except:
    s.close()
    #Cerrar cursor y DB
    cursor.close()
    db.close()
    print("Fin del programa")
    