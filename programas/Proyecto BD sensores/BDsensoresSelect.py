import mysql.connector as mysql
import matplotlib.pyplot as plt #para hacer gráficos

#Conexión a la BD
db= mysql.connect(host="192.168.1.25", user="roger", passwd="1234",database="datosArduino")
cursor = db.cursor()

#Seleccionar elementos de la BD
query= "SELECT * FROM sensores"
cursor.execute(query)
resultados = cursor.fetchall()
db.commit()

print(resultados)

#Cerrar cursor y DB
cursor.close()
db.close()