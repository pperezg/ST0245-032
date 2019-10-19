import numpy as np
file = open("instrucciones.txt","r")
info = file.readlines()
file.close()

listaInstrucciones = []

n = len(info)
listita = []
listita.append(info(0))
listita.append(info(1))

for i in range (2,n-1):
  if len(info(i))== 1 and len(info(i+1)==1):
    listaInstrucciones.append(listita)
    listita = []
    listita.append(info(i))
  
  else:
    listita.append(info(i))
    
m = len(listaInstrucciones)

for j in range(0,m):
  size = listaInstrucciones(j)(0)
  matrix = np.zeros([size, size], dtype = int)
  colors = np.zeros(size, dtype = int)
  cantDeUniones = listaInstrucciones(j)(1)
  for q in range (2,cantDeUniones+2):
    origin = listaInstrucciones(j)(q)(0)
    destination = listaInstrucciones(j)(q)(2)
    matriz[origin][destination] = 1
    matriz[destination][origin] = 1
  colors[0]=2
  possible = true
  for w in range(0,size):
    for i in range(0,size):
      if matriz[w][i]==1:
        if colors[w]==2 and colors[i]==0:
          colors[i]==3
        elif colors[w]==3 and colors[i]==0:
          colors[i]==2
        elif colors[w]==2 and colors[i]==2:
          possible == false
        elif colors[w]==3 and colors[i]==3:
          possible == false
  if possible == true:
    print("BICOLORABLE")
  else:
    print("NOT BICOLORABLE")