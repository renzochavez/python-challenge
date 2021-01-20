import csv
csvpath_output = ("main.txt")
vote_count=0
candidates_list = []
winner_votes = 0
total_candidates = 0
greatest_votes = ["", 0]
candidate_votes = {}

    

with open('Resources/election_data.csv', 'r') as election_csv:
    csv_reader = csv.DictReader(election_csv, delimiter=',')
    header = next(csv_reader)
    
    for row in csv_reader:
        vote_count += 1
        total_candidates = row['Candidate']
        if row['Candidate'] not in candidates_list: 
               candidates_list.append(row['Candidate'])
               candidate_votes[row["Candidate"]] = 1
        else:
             candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1
      
    if (vote_count > winner_votes):
        greatest_votes[1] = candidate_votes
        greatest_votes[0] = row["Candidate"]
    
    
    print("Election Results")
    print("-------------------------")
    print("Total Votes " + str(vote_count))
    print("-------------------------")

    for candidate in candidate_votes:
        print(candidate + " " + str(round(((candidate_votes[candidate]/vote_count)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/vote_count)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
    
candidate_votes

winner = sorted(candidate_votes.items(),)

                
print("-------------------------")
print("Winner: " + str(winner[1]))
print("-------------------------")

with open(csvpath_output, "w") as txt_file:
    
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write(candidate + " " + str(round(((candidate_votes[candidate]/vote_count)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")
    txt_file.write(str(winner))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winner[1]))
    txt_file.write("\n")
    txt_file.write("Total Votes " + str(vote_count))