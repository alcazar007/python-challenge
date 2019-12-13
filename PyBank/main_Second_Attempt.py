## PyBank

'''
* In this challenge, you are tasked with creating a Python script for analyzing
 the financial records of your company. You will give a set of financial data 
 called [budget_data.csv](PyBank/Resources/budget_data.csv). 
 The dataset is composed of two columns: `Date` and `Profit/Losses`.

* Your task is to create a Python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* As an example, your analysis should look similar to the one below:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

* In addition, your final script should both print the analysis to the terminal and export a text file with the results.

'''

# Imports
import os, csv


# CSV Path
data_file = os.path.join("Resources", "budget_data.csv")


#store objects
profit = []
monthly_changes = []
date = []

# Variables

total_months = 0
total_profit = 0
total_change = 0
initial_profit = 0

# Open csv with reader, header, and F statement

with open (data_file, newline="", encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)


# Loop through the data to variables
    for row in csv_reader:
# use count for calculating the number of months in dataset
        total_months = total_months + 1

# need to collect data using .append for greatest increase and decrease in profits
    date.append(row[0])

# need to collect data using .append profit information and calculate the total profit
    profit.append(row[1])
    total_profit = total_profit = int(row[1])

# Calculate the average change in profits 
    final_profit = int(row[1])

# Calculate average change in profit
    monthly_change_profits = final_profit - initial_profit

# Store these monthly changes in a list
    monthly_changes.append(monthly_change_profits)

# calculate total profits by adding total changes = monthly changes
    total_change = total_change + monthly_change_profits

# profits
    initial_profit = final_profit
        
# calculate the average change in profits
average_change_profits = (total_change/total_months)

#Find the max and min change in profit
greatest_increase_profits = max(monthly_changes)
greatest_decrease_profits = min(monthly_changes)

increase_date = date[monthly_changes.index(greatest_increase_profits)]
decrease_date = date[monthly_changes.index(greatest_decrease_profits)]



print("----------------------------")
print("# Finaancial Analysis") 
print("total Months: " + str(total_months) + "\n")
print("Total Profits: " + "$" + str(total_profit) + "\n")
print("Average Change:" + "$" + str(int(average_change_profits)))
print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
print("Greatest Decrease in profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
print("------------------------------------------------------------")

with open('financial_analysis.txt', 'w') as text:
    text.write("------------\n")
    text.write(" Financial Analysis"+ "\n")
    text.write("-------------------------\n\n")
    text.write(" Total Months: " + str(total_months) + "\n")
    text.write(" Total Profits: " + "$" + str(total_profit) + "\n")
    text.write(" Average Change: " + "$" + str(int(average_change_profits)) + "\n")
    text.write(" Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write(" Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write(" -----------------------\n")

