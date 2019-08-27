#diccionarios
#Felipe Lorca

d = {}#Creo el diccionario con {}
# d = {"George":24,"Tom":32}

d["George"] = 24 #Usando la key "George" le doy un valor de edad

# Agrego mas edades usando diferentes key
d["Tom"] = 32
d["Jenny"] = 16

print d["George"] #Muestro el valor usando la key "George"

print d["Tom"]

# print d["Alice"] error por no existe la key

print d["Jenny"]

d["Jenny"] = 20

print d["Jenny"]

d[10] = 100 #key = 10 valor 100

print d[10]

for key, value in d.items(): #con el ciclo for recorro todos los items del diccionario
	#muestros las key y los valores de mi diccionario de forma ordenada 
	print "key:"
	print key
	print "value:"
	print value 
	print ""



