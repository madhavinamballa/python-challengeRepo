import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    total_months=0
    total_profit=0
    max=0
    min=0
    csv_header = next(csvreader)
    for row in csvreader:
        total_months=total_months+1
        total_profit=total_profit+int(row[1])
        if int(row[1])>max:
            max=int(row[1])
            maxmonth=row[0]
        if int(row[1])<min:
            min=int(row[1])
            minmonth=row[0]
        
        
    average=total_profit/total_months
    print("Total Months:",total_months)
    print(f'Total profit/loses: ${total_profit}')
    print(f'Average  Change: ${average}')
    print(f'Greatest Increase in Profits: {maxmonth} (${max})')
    print(f'Greatest decrease in Profits:{minmonth} (${min})')

    
