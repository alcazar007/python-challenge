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

import csv, os

csv_file = os.path.join("Resources","budget_data.csv")


month_count = 0
total_profit = 0
change_list = []
previous = 0
greatest_increase = ["",0]
greatest_decrease = ["",99999999]



with open(csv_file) as budget_data:
    reader = csv.reader(budget_data)
    header = next(reader)


    for x in reader:
        month_count = month_count + 1

        total_profit = total_profit + int(x[1])

        # 867884 - 0 net_change is looking at current value and pervious value and subtracting storing results in change_list of subtracted totals which 
        # we will use to calculate overall net change and subtract total value to calculate average change
        net_change = int(x[1]) - previous 
        previous = int(x[1]) # previous is = 867884
        change_list = change_list + [net_change]

        if net_change > greatest_increase[1]:
            greatest_increase[0] = x[0]
            greatest_increase[1] = net_change
        # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = x[0]
            greatest_decrease[1] = net_change
         
average_netchange = sum(change_list) / len(change_list)

'''
print(month_count)
print(total_profit)
print(average_netchange)
print(greatest_increase)
print(greatest_decrease) '''


print("----------------------------")
print("# Finaancial Analysis") 
print("total Months: " + str(month_count) + "\n")
print("Total Profits: " + "$" + str(total_profit) + "\n")
print("Average Change:" + "$" + str(int(average_netchange)))
print("Greatest Increase in Profits: " + str(greatest_increase) + " ($" + str(greatest_increase) + ")\n")
print("Greatest Decrease in profits: " + str(greatest_decrease) + " ($" + str(greatest_decrease) + ")\n")
print("----------------------------")

with open('tutor_financial_analysis.txt', 'w') as text:
    text.write("------------\n")
    text.write(" Financial Analysis"+ "\n")
    text.write("-------------------------\n\n")
    text.write(" Total Months: " + str(month_count) + "\n")
    text.write(" Total Profits: " + "$" + str(total_profit) + "\n")
    text.write(" Average Change: " + "$" + str(int(average_netchange)) + "\n")
    text.write(" Greatest Increase in Profits: " + str(greatest_increase) + " ($" + str(greatest_increase) + ")\n")
    text.write(" Greatest Decrease in Profits: " + str(greatest_decrease) + " ($" + str(greatest_decrease) + ")\n")
    text.write(" -----------------------\n")











