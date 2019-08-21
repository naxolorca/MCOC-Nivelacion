# BMI calculator
# creo variables con valores adecuados al problema
name1 = "YK"
height_m1 = 2
weight_kg1 = 90

name2 = "YK's sister"
height_m2 = 1.8
weight_kg2 = 70

name3 = "YK's brother"
height_m3 = 2.5
weight_kg3 = 160

def bmi_calculator(name,height_m,weight_kg): #crea la funcion con 3 parametros
	bmi = weight_kg / (height_m ** 2 ) # calcula el bmi
	print "bmi: "
	print bmi #imprime bmi
	if bmi < 25 :#prueba logica para el bmi
		return name + " is not overweight"
	else:# si no se cumple la anterios 
		return name + " is overweight"
	
result1 = bmi_calculator(name1,height_m1,weight_kg1) #variable con la funcion y sus parametros
result2 = bmi_calculator(name2,height_m2,weight_kg2) #variable con la funcion y sus parametros
result3 = bmi_calculator(name3,height_m3,weight_kg3) #variable con la funcion y sus parametros

print result1 #imprimo la variable 
print result2 #imprimo la variable 
print result3 #imprimo la variable 