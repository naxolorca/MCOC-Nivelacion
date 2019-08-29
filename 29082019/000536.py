# Felipe Lorca
# arreglos y cosas basica no los repetire en este video ya wue estan explicado en los 2 anteriores
import numpy as np

a = [1,2,3,4]
b = [10,11,12,13]

output = []

for item1, item2 in zip(a,b): #tomo las dos lista a la vez
	output.append(item1+item2)

print output

g = list(range(1000000))

#%timeit sum(g) no existe aqui
g_array = np.array(g) #lo hago np

#%timeit np.sum(g_array) es mas rapido

# list en python van a buscar los datos numpy los tiene guardado en un espacio

# muestra ejemplo que se pueden hacer con listas numpy dividir multiplicar etc igual que en video anteriores


#001345 muestra datos de numpy como saber dtype dimension etc


#001821 Muestra mas usos de array

print np.sin(a)

# cambia los formatos de los dato en el array
a = np.array([1,2,3,4.0], dtype = "int32")
print a



#002520 muestra omo crear array de mas de una dimension igual que videos anteriores

c = np.array([[10,11,12],[20,21,22]])

print c
# muestra las dimensiones y la forma
print c.ndim
print c.shape

#se puede trasponer nuestra matriz
print a
print a.T # aqui tiene 1 d8imension por lo que es igual


print c

print c.size #muestra el numero de elementos

print c.nbytes # se cuanta memoria estoy ocupando

# muestro como editar y mostrar datos de las listas como en video anterior

#var[lower:upper:step]

g = [1,2,3]

print g[0]

print g[:1] #muestro hasta el primer dato


a = np.arange(25).reshape(5,5) # creo una matriz ordenada de 5x5

print a

red = a[:,1::2] # selecciono la 2 y 4 columna

print red

yellow = a[4] # ultima fila

print yellow

yellow = a[-1] # ultima fila

print yellow
yellow = a[4] # ultima fila

print yellow
yellow = a[-1,:] # ultima fila

print yellow

blue = a[1::2, :3:2] # tomo los que quiero 
print blue

red[-1,-1] = 0 # cambia los 2 por ser la misma memoria
print red
print a

print id(a)
print id(red)

# puedo hacer una copia y se guarda diferente
red.copy()

