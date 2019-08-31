# Felipe Lorca

from matplotlib import pyplot as plt # importo la libreria para plotear

ages_x = [25,26,27,28,29,30,31,32,33,34,35] # lista valores en x

dev_y = [28496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752] # lista eje y

plt.plot(ages_x,dev_y, color="k",linestyle="--",marker=".",label="All Devs") #grafico 1

py_dev_y = [45372,48876,53850,57287,63016,65998,70003,70000,71496,75370,83640] # lista de datos

plt.plot(ages_x,py_dev_y, color="b",marker="o", label="Python") # grafico 2

plt.plot(ages_x,dev_y) # creo grafico
plt.xlabel("Ages") # label en x
plt.ylabel("Median Salary") # label en y
plt.title("Median Salary (USD) by Age") # titulo del grafico

plt.legend(["All Devs", "Python"])

plt.show() # muesdtro el grafico

