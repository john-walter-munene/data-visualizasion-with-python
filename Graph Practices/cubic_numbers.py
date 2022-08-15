import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

# Remoivng outline from data ponts
# Using the color map
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolors='none', s=40)

# Set chart title and label the axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set the range for each axis
plt.axis([0, 5000, 0, 5000**3])

# Svaing the plot automatically
plt.savefig('cubic_plot.png', bbox_inches='tight')
