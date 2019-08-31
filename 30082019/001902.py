# Felipe Lorca

from matplotlib import pyplot as plt # importo la libreria para plotear

print(plt.style.available) #muestra los styles

plt.style.use("fivethirtyeight") # style

plt.xkcd() #style raro

ages_x = [25,26,27,28,29,30,31,32,33,34,35] # lista valores en x


py_dev_y = [45372,48876,53850,57287,63016,65998,70003,70000,71496,75370,83640] # lista de datos

plt.plot(ages_x,py_dev_y, color="#5a7d9a", linewidth=3, label="Python") # grafico 2


js_dev_y = [37810,43515,46823,49293,53437,56373,62375,66674,68745,68746,74583] #lista

plt.plot(ages_x,js_dev_y,color="#adad3b",linewidth=3, label="JavaScript") # creo grafico

dev_y = [28496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752] # lista eje y

plt.plot(ages_x,dev_y, color="#444444",linestyle="--",label="All Devs") #grafico 1


plt.xlabel("Ages") # label en x
plt.ylabel("Median Salary") # label en y
plt.title("Median Salary (USD) by Age") # titulo del grafico

plt.legend() # agrega las leyendas

plt.grid(True) # crea un grid

plt.tight_layout()

plt.savefig("plot.png") # guarda el grafico

plt.show() # muesdtro el grafico

#luego muestra un grafico igual pero con mas datos
