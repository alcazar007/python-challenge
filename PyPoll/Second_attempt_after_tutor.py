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

csv_file = os.path.join("Resources","election_data.csv")


total_votes = 0
candidates_list = []
candidates_total = 0
total_votes_per_candidate = 0
winner_name = []
word = []
votes = [0,0,0,0]
votes_percent_dictionary = {}
votes_total_dictionary = {}


with open(csv_file) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)

    for x in reader:
        total_votes = total_votes + 1

        word = str(x[2])

        # Iterate over the list using for loop
    # values in x[2](could be any name) are being stored in memory or another column 
    # then checking if the values stored when camparing x[2] to word are not in candidates_list
    # then the values are added to candidates_list
        if word not in candidates_list:
            candidates_list.append(x[2])
            votes_total_dictionary[x[2]] = 0
        votes_total_dictionary[x[2]] = votes_total_dictionary[x[2]] + 1

        for y in votes_total_dictionary:
            votes_percent_dictionary[y] = (votes_total_dictionary[y] / total_votes) * 100

print(total_votes)
print(candidates_list)
print(votes_total_dictionary)
print(votes_percent_dictionary)

  
