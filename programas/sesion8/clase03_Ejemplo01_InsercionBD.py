import mysql.connector as mysql
import random

#Conexión a la BD

db= mysql.connect(host="192.168.1.25", user="roger", passwd="1234",database="test")
cursor = db.cursor()

query="INSERT INTO Prueba(valor1, valor2) VALUES (%s,%s)"
valores = (16,15)

#Para crear registros aletatorios
for i in range(40):
    valores =(random.randint(15,30),random.randint(15,30))
    cursor.execute(query, valores)
    db.commit()

continuar= True
while continuar:
    v1= input("Añada el primer valor: ")
    if v1 == "z":
        continuar= False
        
    else:
        v2= input("Añada el segundo valor: ")
        valores= (int(v1), int(v2))
        cursor.execute(query, valores)
        print("Los valores: ")
        print(v1, v2)
        print("Se han introducido correctamente")
        
        db.commit()
    

#cursor.execute(query, valores)

db.commit()

#Cerrar cursor y DB
cursor.close()
db.close()

print("Fin del programa")

