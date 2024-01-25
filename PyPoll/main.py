import csv
import os
csvpath = os.path.join('Resources', 'election_data.csv')
txtpath = os.path.join('analysis', 'election_analysis.txt')

#Define my variables
votes_cast = 0
candidates_list = []
votes_per_candidate = {}
percentage_per_candidate = {}
winner = ""

#Read the File and Skip Header**
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)


    #The total number of votes cast
    for row in csvreader:
        votes_cast += 1
      

#A complete list of candidates who received votes
        candidate = row[2]
        if candidate not in candidates_list:
            candidates_list.append(candidate)
    print("List of candidates", candidates_list)

#Count the number of votes per candidate
    if candidate not in votes_per_candidate:
        votes_per_candidate[candidate] = 1
    else: votes_per_candidate[candidate] += 1

#The percentage of votes each candidate won
for candidate, votes in votes_per_candidate.items():
    if votes == 0:
        percentage_per_candidate[candidate] = 0
    else: percentage_per_candidate[candidate] = (votes / votes_cast) *100
print int:("percentage_per_candidate")


        

        

#The total number of votes each candidate won

#The winner of the election based on popular vote
        

#print(votes_cast)
output = (
    f"Election Results\n"
    f"------------------------\n"
    f"Total Votes: {votes_cast}\n"
    f"------------------------\n"
    
)
with open(txtpath, 'w') as txtfile:
    txtfile.write(output)

    print(output)
# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------