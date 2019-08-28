import numpy as np 
from skimage import io # import skimage
import matplotlib.pyplot as plt # importo pyplot
photo = io.imread("foto.jpg") #trasformo jpe a una matriz

photo_sin = np.sin(photo) # calculo el seno de cada valor en la matriz de forma rapida

print photo_sin

# se puede hacer varios parecidos
print np.sum(photo)
print np.prod(photo)
print np.mean(photo)
print np.std(photo)
print np.var(photo)
print np.min(photo)
print np.max(photo)
print np.argmin(photo)
print np.argmax(photo)

z = np.array([1,2,3,4,5]) # creo un array

print z < 3 #pruebo condiciones logicas y me devuelve en boolean
print z > 3
print z[z>3] # prueba la condicion logica y me da los datos verdaderos

photo_masked = np.where(photo > 100,255,0) # donde el valor sea mayor a 100,remplazara con 255 y si no se cumple con 0

# muestro la imagen
plt.imshow(photo_masked)
plt.show()
# creo los array con np
a_array = np.array([1,2,3,4,5])
b_array = np.array([6,7,8,9,10])

print a_array+b_array # sumo cada valor en misma posicion

print a_array + 30 #le sumo 30 a cada valor 

print a_array * b_array #multiplico cada valor en la misma posicion

print a_array * 10

# producto punto no funciona print a_array @ b_array

plt.imshow(photo[:,:,0].T) # hago el inverso de la foto y rotada
plt.show()

x = np.array([2,1,4,3,5])
print np.sort(x) # ordeno el array de menor a mayor