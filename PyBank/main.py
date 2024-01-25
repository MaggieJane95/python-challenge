import csv
import os
csvpath = os.path.join( 'Resources', 'budget_data.csv')

#Define my Variables
months = 0
list_months_changes = []
net_total_amount = 0
net_changes_profit_losses = []
greatest_increase = ["", 0]
greatest_decrease = ["", 10000000]

# Read my file
with open(csvpath) as budget_data:
    read_file = csv.reader(budget_data)
    header = next(read_file)
    first_row = next(read_file)

    months = months + 1
    net_total_amount = int(first_row[1]) + net_total_amount
    net_previous_total_amount = int(first_row[1])

    for row in read_file:
        months = months + 1
        net_total_amount = int(row[1]) + net_total_amount
        change = int(row[1]) - net_previous_total_amount
        net_changes_profit_losses.append(change)
       

        #list_months_changes.append(row[0])
        list_months_changes += [row[0]]
        net_previous_total_amount = int(row[1])

#Calculate average change
        average_change = sum(net_changes_profit_losses) / len(net_changes_profit_losses)
    
# Determine the greatest increase and decrease in profits
if net_changes_profit_losses:
    max_index = net_changes_profit_losses.index(max(net_changes_profit_losses))
    min_index = net_changes_profit_losses.index(min(net_changes_profit_losses))

    if max_index < len(list_months_changes):
        greatest_increase[1] = max(net_changes_profit_losses)
        greatest_increase[0] = list_months_changes[max_index]

    if min_index < len(list_months_changes):
        greatest_decrease[1] = min(net_changes_profit_losses)
        greatest_decrease[0] = list_months_changes[min_index]
else:
    greatest_increase = ["", 0]
    greatest_decrease = ["", 0]


# Calculate the changes in profit/losses for each month
for i in range(len(net_changes_profit_losses) - 1):
    change = net_changes_profit_losses[i] - net_changes_profit_losses[i + 1]
    net_changes_profit_losses[i] = change


# Calculate the average change
average_change = sum(net_changes_profit_losses) / len(net_changes_profit_losses)

# Determine the greatest increase and decrease in profits
for i in range(len(net_changes_profit_losses)):
    if net_changes_profit_losses[i] > greatest_increase[1]:
        greatest_increase[1] = net_changes_profit_losses[i]
        greatest_increase[0] = list_months_changes[i]

    if net_changes_profit_losses[i] < greatest_decrease[1]:
        greatest_decrease[1] = net_changes_profit_losses[i]
        greatest_decrease[0] = list_months_changes[i]

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${net_total_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")








    




