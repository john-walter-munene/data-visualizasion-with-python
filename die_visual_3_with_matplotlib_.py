from multiprocessing import Value
from unittest import result
from die import Die
import matplotlib.pyplot as plt

# Keep rolling dice as long as program is active.
while True:
    # Make a 100 sides dice
    dice = Die(100)
    
    # Roll the dice 1000 times and get its random number output
    # Analyze the results
    results, rolls = [], []
    for roll_number in range(1, 1001):
        outcome = dice.roll()
        results.append(outcome)
        rolls.append(roll_number)
        
    y_values = rolls
    x_values = results
    
    # Create visualization using Matplotlib
    plt.scatter(y_values, x_values, c='red', edgecolors='none', s=10)
    
    plt.figure(figsize=(10, 6))
    
    plt.show()
    
    keep_running = input("Make another walk? (yes/no): ")
    if keep_running == 'no':
        break
    
        
    

