import matplotlib.pyplot as plt

# Cube

# Nomal value
#x_values = [1, 2, 3, 4, 5]
#y_values = [1, 8, 27, 64, 125]

x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]

#plt.scatter(x_values, y_values, edgecolor='none' , s=40)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

plt.show()
