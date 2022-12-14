import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks as long at the program is active
while True:
    
    # Make a random walk and plot the points
    rw = RandomWalk(50000)
    rw.fill_walk()
    
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    
    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    
    # Set the size of the plotting window.
    plt.figure(figsize=(10, 6))
    
    plt.show()
    
    keep_running = input("Make another walk? (yes/no): ")
    if keep_running == 'no':
        break
    