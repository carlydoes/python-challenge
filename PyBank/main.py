#import os module, csv files, and module for statistics
import os
import csv
import statistics

#path to folder with budget data 
csvpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'budget_data.csv')

totalMonth = 0
totalAmount = 0
greatestIncrease = 0
greatestDecrease = 0
highestMonth = ''
lowestMonth = ''

change = []
monthChanges = []

#open with budget data file
with open(csvpath,newline='') as csvfile:
    #holds content
    csvreader = csv.reader(csvfile,delimiter=',')
    #read first row
    csv_header = next(csvreader)

    #reading each row of data after the header
    for row in csvreader:
        totalMonth += 1
        totalAmount += int(row[1])
        if int(row[1]) > greatestIncrease:
            highestMonth = (row[0])
            greatestIncrease = int(row[1])
        elif int(row[1]) < greatestDecrease:
            lowestMonth = (row[0])
            greatestDecrease = int(row[1])
        change.append(int(row[1]))

for i in range(len(change)-1):
    monthlyChange = (change[i+1] - change[i])
    monthChanges.append(monthlyChange) 

averageChange = statistics.mean(monthChanges)

#print results
print("Financial Analysis")
print("___________________________________")

print("Total Months: " + str(totalMonth))
print("Average Change is: $" + str(round(averageChange, 2)))
print("Total: $" + str(totalAmount))
print("Greatest Increase in Profits: " + str(highestMonth) + "  ($" + str(greatestIncrease) + ")")
print("Greatest Decrease in Profits: " + str(lowestMonth) + "  ($" + str(greatestDecrease) + ")")

#output file
f = open("financial_analysis.txt", "w")
f.write("Financial Analysis")
f.write("___________________________________")

f.write("Total Months: " + str(totalMonth))
f.write("Average Change is: $" + str(round(averageChange, 2)))
f.write("Total: $" + str(totalAmount))
f.write("Greatest Increase in Profits: " + str(highestMonth) + "  ($" + str(greatestIncrease) + ")")
f.write("Greatest Decrease in Profits: " + str(lowestMonth) + "  ($" + str(greatestDecrease) + ")")
