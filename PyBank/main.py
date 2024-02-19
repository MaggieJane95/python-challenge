import os
import csv

#Create path to CSV
budget_data_path = os.path.join('Resources', 'budget_data.csv')
txtpath = os.path.join('Analysis', "budget_analysis.txt") 

#Create my Variables
total_months = 0
net_total_profit_losses = 0
changes_profit_losses = []
month_profit_losses = []
previous_change_profit_losses = 0

#Read my CSV File
with open(budget_data_path) as budget_data:
    csvreader = csv.reader(budget_data, delimiter=',')
    csv_header = next(csvreader)
    first = next(csvreader)

    data = list(csvreader)

#The total number of months / Net proft/losses included in the dataset
    # for row in data:
    #     total_months += 1
    #     net_total_profit_losses += int(row[1])
  
    total_months += 1
    net_total_profit_losses += int(first[1])  
    #current_profit_losses = int(first[1])
    previous_change_profit_losses = int(first[1])
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
for row in data: 
    total_months += 1
    net_total_profit_losses += int(row[1])  
    current_profit_losses = int(row[1])
    change = current_profit_losses - previous_change_profit_losses
    changes_profit_losses.append(change)
    month_profit_losses.append(row[0])
    previous_change_profit_losses = int(row[1])
average_change_profit_losses = sum(changes_profit_losses) / len(changes_profit_losses)

#The greatest increase in profits (date and amount) over the entire period
greatest_increase = max(changes_profit_losses)
# greatest index
greatest_index = changes_profit_losses.index(max(changes_profit_losses))
greatest_month = month_profit_losses[greatest_index]

#The greatest decrease in profits (date and amount) over the entire period
greatest_decrease = min(changes_profit_losses)
least_month_index = changes_profit_losses.index(min(changes_profit_losses))
least_month = month_profit_losses[least_month_index]
#RESULTS
output = (
 f"Financial Analysis\n" 
 f"-----------------------\n"
 f"Total Months: {total_months}\n"
 f"Total: {net_total_profit_losses}\n"
 f"Average Change: {average_change_profit_losses}\n"
 f"Greatest Increase in Profits:{greatest_month} {greatest_increase}\n"
 f"Greatest Decrease in Profits: {least_month} {greatest_decrease}\n"
    
)

with open(txtpath, "w") as txtfile:
    print(output)
    txtfile.write(output)

#RESULTS
#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $22564198
#Average Change: $-8311.11
#Greatest Increase in Profits: Aug-16 ($1862002)
#Greatest Decrease in Profits: Feb-14 ($-1825558)