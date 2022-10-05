import csv
import os
import matplotlib.pyplot as plt
import numpy as np
 
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Candidate Options and candidate votes.
charles_votes = [0,0,0]
diane_votes = [0,0,0]
raymon_votes = [0,0,0]

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)
    # For each row in the CSV file.
    for row in reader:

        # Get the candidate name from each row.
        candidate_name = row[2]

        # Extract the county name from each row.
        county_name = row[1]

        # Conditional statement where vote is added to proper county for each candidate
        if candidate_name == "Charles Casper Stockham":

            if county_name == "Arapahoe":
                charles_votes[0] += 1
            elif county_name == "Denver":
                charles_votes[1] += 1
            elif county_name == "Jefferson":
                charles_votes[2] += 1

        elif candidate_name == "Diana DeGette":

            if county_name == "Arapahoe":
                diane_votes[0] += 1
            elif county_name == "Denver":
                diane_votes[1] += 1
            elif county_name == "Jefferson":
                diane_votes[2] += 1

        elif candidate_name == "Raymon Anthony Doane":

            if county_name == "Arapahoe":
                raymon_votes[0] += 1
            elif county_name == "Denver":
                raymon_votes[1] += 1
            elif county_name == "Jefferson":
                raymon_votes[2] += 1

print(diane_votes)

# Print Visualization of votes per candidate per county. We want a data object in the format of the totals of the candidates votes in each county.
labels = ['Arapahoe', 'Denver', 'Jefferson']
x = np.arange(len(labels))
width = 0.15
fig, ax = plt.subplots(figsize=(12, 6))
rects1 = ax.bar(x - width, raymon_votes, width, label='Raymon Anthony Doane')
rects2 = ax.bar(x + width, charles_votes, width, label='Charles Casper Stockham')
rects3 = ax.bar(x, diane_votes, width, label='Diane Degette')

# Axis labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Vote Count')
ax.set_title('Votes by County and Candidate')
ax.set_xticks(x, labels)
ax.legend()
#ax.set_yscale("log")
ax.bar_label(rects1)
ax.bar_label(rects2)
ax.bar_label(rects3)
fig.tight_layout()
plt.show()