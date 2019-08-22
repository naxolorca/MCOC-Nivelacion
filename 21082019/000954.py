b = ["banana", "apple", "microsoft"] # creo una lista con 3 str
print b # muestro b
temp = b[0] # creo una variable temp con el primer valor de la lista

b[0] = b[2] #al primer elemento de la lista le doy el valor del 3

b[2] = temp # le doy al 3 valor de la lista el mismo valor que temp

print b # muestro la lista modificafa

b[0], b[2] = b[2], b[0] # forma rapida sin tener que definir variables extras
print b