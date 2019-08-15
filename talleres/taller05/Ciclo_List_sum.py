import matplotlib.pyplot as plt
import time

lista = [4, 2, 5, 7, 3]
suma = 0
for i in lista:
    suma = suma + i
print(suma)

plt.plot(lista,lista)
plt.show()
