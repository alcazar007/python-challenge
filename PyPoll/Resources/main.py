'''
## PyPoll

![Vote-Counting](Images/Vote_counting.png)

* In this challenge, you are tasked with helping a small, rural town
modernize its vote-counting process. (Up until now, Uncle Cleetus had 
been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv).
 The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 
 Your task is to create a Python script that analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* As an example, your analysis should look similar to the one below:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```

* In addition, your final script should both print the analysis to the terminal and export a text file with the results.
'''

# Imports
import os, csv

# CSV Path
data_file = os.path.join("election_data.csv")


# Store Objects
database_total_votes = []
candidates_with_votes = []
store_candidates_votes = []
winner = []

# Variables 
total_votes = 0
vote_percents = 0

# Open csv with reaser, header, and F statement
with open (data_file, newline="", encoding="UTF=8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)

# Loop through the data to variables
    for row in csv_reader:
        total_votes = total_votes +1
     
database_total_votes = total_votes
print(database_total_votes)


# A complete list of candidates who received votes  `Voter ID`, `County`, and `Candidate`
candidates_with_votes.append(row[2])
candidates_with_votes = candidates_with_votes
print(candidates_with_votes)

