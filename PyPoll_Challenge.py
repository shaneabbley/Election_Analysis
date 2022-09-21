# -*- coding: UTF-8 -*-

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("results", "election_results.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# County list and county votes dictionary.
counties = []
counties_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track the largest county and county voter turnout.
largestcounty = ""
largestcountyvotes = 0
largestcountypercentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # If statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in counties:

            # Add the existing county to the list of counties.
            counties.append(county_name)

            # Begin tracking the county's vote count.
            counties_votes[county_name] = 0

        # Add a vote to that county's vote count.
        counties_votes[county_name] += 1



# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"County Votes:\n")

    print(election_results, end="")

    txt_file.write(election_results)

    # For loop to get the county from the county dictionary.
    for county_name in counties_votes:

        # Retrieve the county vote count.
        votes2 = counties_votes[county_name]
        # Calculate the percentage of votes for the county.
        votes2percentage = 100*(float(votes2)/float(total_votes))

        # Print the county results to the terminal.
        print("-------------------------")
        print(str(county_name) + " County")
        print("Total votes: " + str(votes2))
        print(f"This counties percentage of all votes: {votes2percentage:.1f}%")

        # Save the county votes to a text file.
        county_results = (f"{county_name}: {votes2percentage:.1f}% ({votes2:,})\n")
        txt_file.write(county_results)
        # print(county_results)

        # Write an if statement to determine the winning county and get its vote count.
        if (votes2 > largestcountyvotes):
            largestcounty = county_name
            largestcountyvotes = votes2
            largestcountypercentage = votes2percentage

    # Print the county with the largest turnout to the terminal.
    print(f"-------------------------")
    print(f"Largest County Turnout: {largestcounty}")
    print(f"-------------------------\n")


    # Save the county with the largest turnout to a text file.
    largestcountywrite = (
        f"-------------------------\n"
        f"Largest County Turnout: {largestcounty}\n"
        f"-------------------------\n")

    txt_file.write(largestcountywrite)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winning Candidate: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage of Votes: {winning_percentage:.1f}%\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
