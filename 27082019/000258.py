import numpy as np  #importo numpy

z = np.linspace(2,10,5) #creo un array desde 2 a 10 con 5 float
print z

z = np.array([10,20]) # puedo poner lista en un array
print z

b_list = [[9,8,7,6,5,4,3],[1,2,3,4,5,6,7]]# lista con listas
z= np.array([b_list]) # creo un array
print z

z.shape


np.random.seed(0) # da un inicio al "random"
z1 = np.random.randint(10,size=6) # crea un array random int de 6
print z1
#muestra nunmeros de la lista
print z1[0]
print z1[0:2]
print z1[-1]
