import numpy as np
info = ["3","3","0 1","1 2","2 0","3","2","0 1","2 1","9","8","0 1", "0 2", "0 3", "0 4", "0 5", "0 6", "0 7", "0 8"] #Datos con instrucciones
listaInstrucciones = [] #Lista con diferentes paquetes de instrucciones

n = len(info)
listita = []
listita.append(info[0])
listita.append(info[1])

for i in range (2,n):
  if len(info[i])== 1 and len(info[i+1])==1:
    listaInstrucciones.append(listita)
    listita = []
    listita.append(info[i])
  
  else:
    listita.append(info[i])
listaInstrucciones.append(listita)
   
m = len(listaInstrucciones)

for j in range(0,m):
  size = int(listaInstrucciones[j][0])
  matrix = np.zeros([size, size], dtype = int)
  colors = np.zeros(size, dtype = int)
  cantDeUniones = int(listaInstrucciones[j][1])
  for q in range(2,cantDeUniones+2):
    origin = int(listaInstrucciones[j][q][0])
    destination = int(listaInstrucciones[j][q][2])
    matrix[origin][destination] = 1
    matrix[destination][origin] = 1
  colors[0]=2
  possible = True
  for w in range(0,size):
    for g in range(0,size):
      if matrix[w][g]==1:
        if colors[w]==2 and colors[g]==0:
          colors[g]=3
        elif colors[w]==3 and colors[g]==0:
          colors[g]=2
        elif colors[w]==2 and colors[g]==2:
          possible = False
        elif colors[w]==3 and colors[g]==3:
          possible = False
  print(matrix)
  print(colors)
  if possible == True:
    print("BICOLORABLE")
  else:
    print("NOT BICOLORABLE")