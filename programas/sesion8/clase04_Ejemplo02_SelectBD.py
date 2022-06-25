import mysql.connector as mysql
import matplotlib.pyplot as plt #para hacer gráficos

ejex =[]
ejev1 =[]
ejev2 =[]

#Conexión a la BD
db= mysql.connect(host="192.168.1.25", user="roger", passwd="1234",database="test")
cursor = db.cursor()

#Seleccionar elementos de la BD
query= "SELECT * FROM Prueba"
cursor.execute(query)
resultados = cursor.fetchall()
db.commit()

#Imprimir elementos en pantalla
for x in resultados:
        ejex.append(x[0])
        ejev1.append(x[1])
        ejev2.append(x[2])
        print(x)

#Cerrar cursor y DB
cursor.close()
db.close()

#Hacer un gráfico con los valores de la BD
plt.plot(ejex, ejev1, label="valor1")
plt.plot(ejex, ejev2, label="valor2")
plt.legend()
plt.xlabel("id")
plt.ylabel("valores")
plt.title("Selección")
plt.show()


print("Fin del programa")