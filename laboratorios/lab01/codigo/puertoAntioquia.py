import matplotlib.pyplot as plt
import timeit
import sys

def opciones1por2(n):
    if n<=2:
        return n
    else:
        return opciones1por2(n-2) + opciones1por2(n-1)

sys.setrecursionlimit(70)
print(opciones1por2(5))

a = []
tiempos = []
for f in range (1,50):
    a.append(f)
    st = timeit.default_timer()
    opciones1por2(f)
    tiempos.append((timeit.default_timer()-st)*1000)

plt.plot(a,tiempos,'ro')
plt.axis([0,50,0,3000])
plt.ylabel('tiempo en milisegundos')
plt.xlabel('largo del arreglo')
plt.show()

print(tiempos[49])