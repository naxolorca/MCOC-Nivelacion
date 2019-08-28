import numpy as np 
from skimage import io # import skimage
import matplotlib.pyplot as plt # importo pyplot


photo = io.imread("foto.jpg") #trasformo jpe a una matriz
print type(photo)
print photo.shape # puestro las dimensiones

plt.imshow(photo) #paso de matriz a foto
plt.show() # muestro la foto

plt.imshow(photo[::-1]) # doy vuelta en el eje x
plt.show()

plt.imshow(photo[:,::-1]) # imagen espejo por dar vuelta en eje y
plt.show()

plt.imshow(photo[50:150,150:280]) # muestro solo el "cuadrado que quiero"
plt.show()

plt.imshow(photo[::2,::2]) #ocupo la mitad de tamano
plt.show()


