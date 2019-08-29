#Felipe Lorca

# numpy es mejor porque ocupa menos memoria y es mas rapido
import numpy as np

a = np.array([2,3,4]) # creo array np
print a

a = np.arange(1,12,2) # creo una lista entre el 1 y el 12 con diferencia de 2

print a

a = np.linspace(1,12,6) # creo una lista entre el 1 y el 12 con 6 elementos

print a


print a.reshape(3,2) # muestro el arreglo ordenado como matriz

a = a.reshape(3,2) #guarda el cambio

print a.size # muestra cuantos elementos son

print a.shape # muestra como esta ordenbado la matriz

print a.dtype # muestra el tipo de los elementos

print a.itemsize  #muestra cuantos bits ocupa

b = np.array([(1.5,2,3),(4,5,6)]) #crea un array de 2 dimensiones

print b

print a < 4 # compara cada elemento y da booleano

print a * 3 # multiplico cada valor por 3

a*=3 # guarda
print a

a = np.zeros((3,2))# crean una matriz de 0 en float
print a
a = np.ones((2,3)) # mismo con 1
print a

a = np.ones(10) # arreglo de 1
print a

a = np.array([2,3,4], dtype =np.int16) # creo un arreglo en un formato con menos memoria

print a

a = np.random.random((2,3)) # arreglo random
print a

np.set_printoptions(precision=2,suppress=True) #digo como mostrar los datos
print a

a = np.random.randint(0,10,5) # arreglo random

print a

#util
print  a.sum()
print a.min()
print a.max()
print a.mean()
print a.std()

a = np.random.randint(1,10,6) # arreglo random
a = a.reshape(3,2) #ordena en mas dimensiones
print a
#util
print a.sum(axis=1)
print a.sum(axis=0)

#data = np.loadtxt("data.txt", dtype=np.uint8, delimiter=",",skiprows=1) cargo archivo de texto con las condiciones que yo quiero

a = np.arange(10) # crea array hasta el 10

print a
np.random.shuffle(a) #mezclo el orden
print a
# elijo un numero random
print np.random.choice(a)

print np.random.choice(a)

print np.random.random_integers(5,10,2) #random del 5 al 10 2 integer
