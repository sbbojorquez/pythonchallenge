import os
import csv

candidates = []

csvpath = os.path.join("..", "Resources", "week-3-python_homework_PyPoll_Resources_election_data.csv")

#The total number of votes cast
with open(csvpath, "r")  as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    total = len(list(csvreader))
    print(total)

#A complete list of candidates who received votes
with open(csvpath, "r")  as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for line in csvreader:
        candidates.append(line[2])

    candidate_list = list(set(candidates))
    print(candidate_list)
        

#The percentage of votes each candidate won

with open(csvpath, "r")  as csvfile:
    counting = 0
    csvreader = csv.reader(csvfile)
    next(csvreader)
    
    for line in candidate_list:
        eachcandidate = line
        counting = 0
        for line2 in candidates:
            if eachcandidate == line2:
                counting = counting + 1
        
        
        
        print(f"{eachcandidate} had {counting} votes")
           




  





#The total number of votes each candidate won

#The winner of the election based on popular vote.