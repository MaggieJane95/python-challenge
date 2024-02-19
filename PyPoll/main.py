import csv
import os
csvpath = os.path.join('Resources', 'election_data.csv')
txtpath = os.path.join('analysis', 'election_analysis.txt')

#Read the CVS File / Skip header
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #print(f"Header: {csv_header}")

# Define my variables
    total_votes_cast = 0
    all_candidates = []
    candidate_votes = {}
    
# The total number of votes cast
    for row in csvreader:
        total_votes_cast += 1
        
        # A complete list of candidates who received votes
        candidate = row[2]
        if candidate not in all_candidates:
            all_candidates.append(candidate)
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1

    #Determine Winner based on highest number of votes
    winner = max(candidate_votes, key=candidate_votes.get)      

    #Percentage Per Candidate
    percentage_per_candidate = {
        candidate: (votes / total_votes_cast) * 100 for candidate, 
        votes in candidate_votes.items()
    }

    output = (
    f"Election Results\n" 
    f"-----------------------\n"
    f"Total Votes: {total_votes_cast}\n"
    f"------------------------\n"
    
    )
    with open(txtpath, "w") as txtfile:
        txtfile.write(output)
        print(output)
   
        for candidate in all_candidates:
            votes = candidate_votes[candidate]
            percentage = percentage_per_candidate[candidate]
            result = f"{candidate}: {percentage:.3f}% ({votes})\n"
            txtfile.write(result)
            print(result)
       
        txtfile.write("-----------------------\n")
        txtfile.write(f"Winner:  {winner}\n")
        txtfile.write("-----------------------\n")
        print("-----------------------\n")
        print(f"Winner:  {winner}\n")
        print("-----------------------\n")
 

   



#The winner of the election based on popular vote
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
