import numpy as np

a = np.array([3,-1,-2,4,-6,8])
print a

negatives = a < 0 #boolean

print a[negatives] 

print a[a<0] #muestro negativos
a[a<0] = 0 # cambio los valores negativos

print a


#mas ejemplo de bolean

#a > 3 and a < 8 error por mas de un boolean en el and

print (a <8).any()

print (a > 3 )&(a<8) # operador para array

print a

f = 6
g = 9
print f+g

print f.__add__(g) #suma

print np.nonzero(negatives) #busco la posicion de los true

print a
a.sort() #ordeno
print a

a = np.array([10,1,20])
b = np.array([2,3,20])

print a>b # compara los array 

#nonzero sirve para la posicion del boolena true

print a

subset = a[[0,2]] #agarro el 0 y 2 lugar
print subset

print a.flags.owndata
print a is subset


# modifico array
subset[0]= -1
print subset
print a

a[-1] = 100

print a


a = np.arange(25).reshape(5,5) #creo matriz
print a%3

print a[a%3] #no doy boolean doy lista de listas

print a % 3 == 0
print a [a%3==0] # me da los numeros divisbles en 3


print np.nan

output = np.empty_like(a) #nuevo array con la misma forma podria dar culaquier cosa en memoria
print output

output.fill(np.nan)
print output

output = np.empty_like(a, dtype = "float")

output.fill(np.nan)
print output
print a

mask = a%3 == 0
output[mask] = a[mask] # pongo en la matriz los numeros donde deberian
print output

print np.where(a%3 == 0,a,np.nan) #rellena con 2 valores dependiendo si cumple o no la condicion



