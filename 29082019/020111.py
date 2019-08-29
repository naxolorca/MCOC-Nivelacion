#multi dimesion

import numpy as np

#muestro nan
print np.nan + 6

print np.sum([1,np.nan,9])

print np.nansum([1,np.nan,9]) 

a = np.array([1,2,3])

print np.sum(a) #es una funcion

print a.sum() # es un metodo


a = np.arange(24).reshape(6,4)

print a.shape

print a.mean(axis=1).shape #quierso saber si estoy viendo lo que quiero

channel_means = a.mean(axis=1)

print channel_means

# archivo de texto que no se encuentra disponible...

from numpy import loadtxt



'''
No funciona por no tener el texto
son desafios ocupando lo aprendido

#data = loadtxt("wind.data") no tengo el texto

dates = data[:,:3]
winds = data[:,3:]

print winds.mean(), winds.min(),winds.max(), winds.std()

print winds.min(axis=0)

print winds.min(axis=1)

print winds.argmax(axis=1)

row, col = np.where(winds == winds.max())

row, col = np.unravel_index(winds.argmax(), winds.shape)

row = winds.max(axis=1).argmax()


print dates[row]


january = dates[:, 1] == 1:

winds[january, :].mean(axis=0)


'''
