import time

#time.time indica el tiempo que ha pasado desde 1975
print(time.time())

for i in range(10):
    print(i)
    #Permite parar la velocidad del programa
    time.sleep(0.2)
    
print(time.time())
    
