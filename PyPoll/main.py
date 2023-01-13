#import os module and reading CVS files
import os
import csv

#path to folder with election data
csvpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'election_data.csv')

#open with election data file
with open(csvpath,newline='') as csvfile:

    #holes content
    csvreader = csv.reader(csvfile,delimiter=',')
    #read first row
    csv_header = next(csvreader)
    candidate_list = [candidate[2] for candidate in csvreader]

    #reading each row od data after the header
    for row in csvreader:
        totalVotes += 1
        if row[2] not in votesPerCandidate:
            votesPerCandidate[row[2]] = 1
        else:
            votesPerCandidate[row[2]] += 1

#calculate the total votes
total_votes = len(candidate_list)

#list of candidates with number of votes
candidates_info = [[candidate,candidate_list.count(candidate)]for candidate in set(candidate_list)]
votesPerCandidate = {}


print("Election Results")
print("------------------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------------------")

for candidate in candidates_info:
    percent_votes = (candidate[1] / total_votes) * 100
    print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})')

print("------------------------------------")
print(f"Winner:{candidates_info[0][0]}")
print("------------------------------------")


#text file
f = open ("election_results.txt","w")
f.write("Election Results")
f.write('\n')
f.write("------------------------------------")
f.write('\n')
f.write(f"Total Votes: {total_votes}")
f.write('\n')
f.write("------------------------------------")
f.write('\n')

for candidate in candidates_info:
    percent_votes = (candidate[1] / total_votes) * 100
    print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})')

f.write("------------------------------------")
f.write('\n')
f.write(f"Winner:{candidates_info[0][0]}")
f.write('\n')
f.write("------------------------------------")
 
