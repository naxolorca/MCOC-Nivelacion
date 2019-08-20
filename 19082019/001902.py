name = "YK" #variable con string
height_m = 2 #variable con int
weight_kg = 90 #variable con int

bmi = weight_kg / (height_m ** 2)  # variable en donde calculo el bmi
print "bmi:" # imprimo
print bmi # imprimo la variable
if bmi < 25: # primera condicion logica
	print name # imprime variable indentada
	print "is not overweight" #print indentado
else: # si no se cumple ninguna condicion logica
	print name # print variable
	print "is overweight" #print indentado