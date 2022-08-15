import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# Remoivng outline from data ponts
# Using the color map
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)

# Set chart title and label the axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set the range for each axis
plt.axis([0, 1100, 0,  1100000])

# Svaing the plot automatically
plt.savefig('squares_plot.png', bbox_inches='tight')
