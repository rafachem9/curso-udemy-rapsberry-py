import mysql.connector as mysql

#Conexión a la BD
db= mysql.connect(host="192.168.1.25", user="roger", passwd="1234",database="test")
cursor = db.cursor()

#Update
query= "UPDATE Prueba SET valor1=%s, valor2=%s WHERE id=%s"
valores= (5,6, 10)
cursor.execute(query, valores)

db.commit()

#Cerrar cursor y DB
cursor.close()
db.close()


print("Fin del programa")