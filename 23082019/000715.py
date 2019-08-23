given_list = [5,4,4,3,1] #creo una lista

total3 = 0
i = 0
while  i < len(given_list) and given_list[i] > 0: # loop con 2 condiciones
	total3 += given_list[i] #sumo el valor de la lista
	i += 1 # sumo al contador
print total3
	
given_list2 = [5,4,4,3,1,-2,-3,-5] #creo una lista
total4 = 0 # variable total
for element in given_list2: # loop for 
	if element <= 0: #condicional para los elementos negativos
		break # si es negativo rompo el ciclo
	total4 += element # si llego aqui sumo
print total4

total5 = 0
i = 0 # contador
while True: #loop siempre correcto
	total5 += given_list2[i]
	i += 1 # sumo contador
	if given_list2[i] <= 0: #rompo el ciclo 
		break
print total5