import os
import csv

csvPath = os.path.join("../Resources", "election_data.csv")


votes = 0
candidate_dict = {}
current_winner = 0
Summary = []


with open(csvPath, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader = next(csvreader)

    #The total number of votes included in the dataset
    for row in csvreader:

        votes = votes + 1
        
        name = row[2]

        #The total number fo votes for each candidate
        if name in candidate_dict:

                candidate_dict[name] = candidate_dict[name] + 1

        else: 
        
                candidate_dict[name] = 1

print("Election Results")
Summary.append("Election Results")
print("------------------------------------")
Summary.append("------------------------------------")        

print(f"Total Votes: {votes}")
Summary.append(f"Total Votes: {votes}")
print("------------------------------------")
Summary.append("------------------------------------")


for name in candidate_dict:

        #Percent votes for each candidate
        candidate_percent = (candidate_dict[name] / votes) * 100

        print(f"{name}: {round(candidate_percent, 2)}% ({candidate_dict[name]})")
        Summary.append(f"{name}: {round(candidate_percent, 2)}% ({candidate_dict[name]})")

        #Declare the winner
        if candidate_dict[name] > current_winner:

                current_winner = candidate_dict[name]
                winner_name = name


print("------------------------------------")        
Summary.append("------------------------------------")

print(f"Winner: {winner_name}")
Summary.append(f"Winner: {winner_name}")


output_path = os.path.join("PyBank.txt")

with open("PyPoll.txt","w") as PyPoll_text:
   
    PyPoll_text.write('\n'.join(Summary))
