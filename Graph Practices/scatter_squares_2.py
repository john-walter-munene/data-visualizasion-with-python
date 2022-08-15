import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# Remoivng outline from data ponts
# Defining custom colors
plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolors='none', s=40)

# Set chart title and label the axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set the range for each axis
plt.axis([0, 1100, 0,  1100000])

plt.show()