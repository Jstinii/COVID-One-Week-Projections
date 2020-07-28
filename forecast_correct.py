"""
Author: Justin Ngo
Date: 7/27/20
Description: Script to create basic graph of cumulative deaths of a certain area given csv file
csv file must follow the same guidelines as in sample csv
"""
import csv
import matplotlib.pyplot as plt
import numpy as np

#Planning to change to Plotly from Matplotlib

# Plot Initial Settings
plt.style.available
print(plt.style.available)
plt.style.use('bmh')

with open('sample.csv', 'r') as csv_file: # read csv file
    csv_reader = csv.reader(csv_file) # create csv.reader object
    next(csv_reader)

    # Adding Time Arrays for x , very inefficient I know
    x_DELPHI = []
    x_IMHE = []
    x_LANL = []
    # Adding Death Arrays for y
    x_actual = []
    y_DELPHI = []
    y_IMHE = []
    y_LANL = []
    y_actual = []
    # Adding error arrays
    error_DELPHI = []
    error_IMHE =[]
    error_LANL = []

    for row in csv_reader:
        if row[0] == '': # No more rows that has data in, end for loop
            continue

        x_actual.append((row[0]))
        y_actual.append(int(row[3]))

        if row[2] == 'DELPHI':
            x_DELPHI.append((row[0]))
            y_DELPHI.append(int(row[1]))
            error_DELPHI.append(abs(((int(row[3]) - int(row[1]))) / int(row[3]))) # Average calculation

        elif row[2] == 'IMHE':
            x_IMHE.append((row[0]))
            y_IMHE.append(int(row[1]))
            error_IMHE.append(abs(((int(row[3]) - int(row[1]))) / int(row[3])))

        elif row[2] == 'LANL':
            x_LANL.append((row[0]))
            y_LANL.append(int(row[1]))
            error_LANL.append(abs(((int(row[3]) - int(row[1]))) / int(row[3])))

# Print errors to console and #
print('Error of IMHE', np.mean(error_IMHE)*100,'%')
print('Error of DELPHI', np.mean(error_DELPHI)*100,'%')
print('Error of LANL', np.mean(error_LANL)*100,'%')

#Creation of table
plt.plot(x_DELPHI,  y_DELPHI, color='g', linestyle='--', marker='o', linewidth=2, label = 'MIT Delphi')

plt.plot(x_IMHE,  y_IMHE, color='b', linestyle='--', marker='o', linewidth=2, label = 'IMHE')

plt.plot(x_LANL,  y_LANL, color='y', linestyle='--', marker='o', linewidth=2, label = 'LANL')

plt.plot(x_actual,  y_actual, color='k',  marker='o', label = 'Reported Amount')


plt.xlabel('Date')
plt.ylabel('Cumulative Deaths')
plt.title('Forecast of COVID Models from 1 week before')

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig('plot.png')

plt.show()