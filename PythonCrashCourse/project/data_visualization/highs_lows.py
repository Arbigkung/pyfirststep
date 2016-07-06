import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get high temperatures from file.
#filename = 'input/death_valley_2014.csv'
filename = 'input/Bangkok-May2016.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])       
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing_date')
        else:
            dates.append(current_date)
            lows.append(low)
            highs.append(high)
 
    print(highs)

# Plot data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
plt.title("Daily high and low tempurature- 2014", fontsize=24)
plt.xlabel('', fontsize=20)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
