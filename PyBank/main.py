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
import os
import csv

# CSV Path

data_file = os.path.join('..','Resources','budget_data.cvs')




# Reading CSV module
with open(data_file, newline='', encoding='utf-8') as csv_file:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csv_file, delimiter=',')


print(csvreader)

# Read the header row first
csv_header = next(csvreader)
print(f"CSV Header: {csv_header}")

# Read each row of data after the header
for row in csvreader:
    print(row)