#Felipe Lorca 
# for loopa 
a=["banana","apple","microsoft"] # lista con 3 str

for element in a:#recorro con el for la lista, cada elemente es element
	print element #printeo element en el instante
	print element #printe0 element en el instante

b = [20,10,5] # lista de int
total = 0 #creo una variable total
for e in b: # recorro b con cada elemente llamado a
	total = total + e # totlat es total viejo mas e
print total # muestro el resultado final

# 1,2,3,4
c = list(range(1,5)) # creo una lista de forma radica como se muestra de 1 a 4

print c # muestro la lista

total2 = 0 # variable donde guardo valor
for i in range(1,5):  #recorro la lista que se crea con range desde el 1 al 4
	total2 += i #sunmo el valor del elemento i a la variable total2
print total2

print list(range(1,8)) #printeo la lista del 1 al 7

print 4%3 #division que da el resto

print 5%3#division que da el resto

print 1%3#division que da el resto

print 6%3#division que da el resto

total3 = 0 # creo varaible para almacenar
for i in range(1,8): # recorro la lista
	if i % 3 == 0:#veo su es multiplo de 3
		total3 += i#sumo si es multipo de 3
print total3

total4 = [] # creo una lista para almacenar
for i in range(1,100): # recorro de 1 a 99
	if i % 3 == 0 or i % 5 == 0 : # veo si es multiplo de 3 o de 5
		total4.append(i)# agrego a mis lista

print total4 # muestro mi lista
print sum(total4) #muestro la suma
