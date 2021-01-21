import os
import csv

csvpath = os.path.join("week-3-python_homework_PyBank_Resources_budget_data.csv")


#The total number of months included in the dataset

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    Lines = len(list(csvreader))
    print(f"{Lines}")
    total = 0
#The net total amount of "Profit/Losses" over the entire period
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    total = 0
    for line in csvreader:
        total += int(line[1])
    print(total)

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    before = 0
    changetotal = 0
    y = 0
    for line in csvreader:
        if before != 0:
            change = int(line[1]) - int(before)
            changetotal = int(change) + int(changetotal)
            before = line[1]
            y = y + 1
        else:
            before = line[1]
    averagechange = changetotal / y

        
    print(averagechange)

#The greatest increase in profits (date and amount) over the entire period   

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    before = 0
    Maxchange = 0
    for line in csvreader:
        if before != 0:
            change = int(line[1]) - int(before)
            if change > Maxchange:
                Maxchange = change
                Maxmonth = line[0]
            before = line[1]
        else:
            before = line[1]
    print(f"{Maxmonth} with {Maxchange}" )

#The greatest decrease in losses (date and amount) over the entire period        
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    before = 0
    Maxloss = 0
    for line in csvreader:
        if before != 0:
            change = int(line[1]) - int(before)
            if change < Maxloss:
                Maxloss = change
                Minmonth = line[0]
            before = line[1]
        else:
            before = line[1]
    print(f"{Minmonth} with {Maxloss}" )
        







