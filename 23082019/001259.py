given_list3 = [7,5,4,4,3,1,-2,-3,-5,-7]

total = 0
i = 0
while True : #loop infinito
	if given_list3[i] <= 0: #rompo el ciclo 
		total += given_list3[i] # sumo los negativos
	i += 1 #aumento el contador
	if i >= len(given_list3): # condicion para que el contador no pase a la lista
		break
print total # muestro el total