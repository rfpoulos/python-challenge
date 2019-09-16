import csv
import os

election_data_raw = os.path.join("Resources", "election_data.csv")

with open(election_data_raw) as election_data:
	reader = csv.reader(election_data)

	header = next(reader)

	first_row = next(reader)

	total_votes = 1
	candidate_votes = {}

	for row in reader:
		total_votes += 1
		if row[2] in candidate_votes:
			candidate_votes[row[2]] += 1
		else:
			candidate_votes[row[2]] = 1

def get_candidate_string(candidates, total_votes):
	string = ""
	for candidate in candidates:
		percent_of_vote = int((candidates[candidate] / total_votes) * 100)
		string += f'{candidate} : {candidates[candidate]} ({percent_of_vote}%) \n'
	return string

def get_winner(candidates):
	current_winner = {}
	highest_votes = 0
	for candidate in candidates:
		if candidates[candidate] > highest_votes:
			current_winner = candidate
			highest_votes = candidates[candidate]
	return current_winner

summary = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------

{get_candidate_string(candidate_votes, total_votes)}
-------------------------
Winner: {get_winner(candidate_votes)}
-------------------------
"""

print(summary)

output_file = os.path.join("Resources", "election_summary.txt")
with open(output_file, "w") as txt_file:
    txt_file.write(summary)