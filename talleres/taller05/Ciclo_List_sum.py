import matplotlib.pyplot as plt 
import timeit
import sys

lista = [4, 2, 5, 7, 3]

def suma(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma

a = []
tiempos = []
for f in range (1,40000):
    a.append(f)
    start_time = timeit.default_timer()
    suma(a)
    tiempos.append(timeit.default_timer()-start_time)

plt.plot(a,tiempos,'ro')
plt.axis([0,40000,0,0.1])
plt.ylabel('tiempo en segundos')
plt.xlabel('largo del arreglo')
plt.show()