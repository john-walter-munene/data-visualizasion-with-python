import csv
from email import header
from fileinput import filename
import matplotlib.pyplot as plt
from datetime import datetime

# Extracting and reading data.
# Get dates and high temperatures from the file
file_name = 'sitka_weather_07-2014.csv'
with open (file_name) as f_n:
    reader = csv.reader(f_n)
    header_row = next(reader)
    
    # Printing headers and their positions.
    for index, column_header in enumerate(header_row):
            print(index, column_header)
            
    # Actual Get date and high temperatures from the file.
    print("\nHigh Temperatures")
    dates, highs, lows = [], [], []
    for row in reader:
        # Dates 
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        
        # Converting the strings into ints that can be read by the matplotlib
        high = int(row[1])
        highs.append(high)
        
        low = int(row[3])
        lows.append(low)
        
    print(highs)
    
# Plot the data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')

# Shading an area in the chart
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format the plot
plt.title("Daily High and Low Temperatures - 2014", fontsize = 24) 
plt.xlabel('', fontsize =16)
plt.ylabel("Temperature (F)", fontsize =16 )
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize=16) 

# Draw the visual
plt.show()      
    
    