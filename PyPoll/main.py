import csv

csvname = "election_data.csv"

with open(csvname, newline = "") as electionfile:
    file_read = csv.reader(electionfile, delimiter = ",")

    file_head = next(file_read)

    vote_count = 0

    candidate_list = []
    totalcandidate = []


    for row in file_read:
        vote_count += 1
        voter = row[0]
        county = row[1]
        candidate = row[2]
        totalcandidate.append(candidate)
        
        # unique list of candidates
        if candidate not in candidate_list:
            candidate_list.append(candidate)
        

    # evaluate candidate column and make list of candidate votes
    khantotal = [vote for vote in totalcandidate if vote == "Khan"]
    correytotal = [vote for vote in totalcandidate if vote == "Correy"]
    litotal = [vote for vote in totalcandidate if vote == "Li"]
    tooleytotal = [vote for vote in totalcandidate if vote == "O'Tooley"]

    # convert list of candidate votes to vote count number value
    khancount = int(len(khantotal))
    correycount = int(len(correytotal))
    licount = int(len(litotal))
    tooleycount = int(len(tooleytotal))

    candidatetotal = khancount + correycount + licount + tooleycount

    # candidates percentage of total votes calculation
    khanpercent = round(khancount/candidatetotal*100,3)
    correypercent = round(correycount/candidatetotal*100,3)
    lipercent = round(licount/candidatetotal*100,3)
    tooleypercent = round(tooleycount/candidatetotal*100,3)

print("Election Results")
print("---------------------")
print("Total Votes: " + str(candidatetotal))
print("---------------------")
print(str(candidate_list[0]) + ": " + str(khanpercent) + "% (" + str(khancount) + ")")
print(str(candidate_list[1]) + ": " + str(correypercent) + "% (" + str(correycount) + ")")
print(str(candidate_list[2]) + ": " + str(lipercent) + "% (" + str(licount) + ")")
print(str(candidate_list[3]) + ": " + str(tooleypercent) + "% (" + str(tooleycount) + ")")
print("---------------------")
print("Winner: " + str(candidate_list[0]))
print("---------------------")
