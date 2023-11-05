# Rutgers Data Boot Camp Module 3 Challange
# Leonid Lyakhovich

# Part 2: Py Poll

# import statments
import os, csv

cpath = os.getcwd()


# Set Path of CSV file
csvpath = os.path.join(cpath,"PyPoll","Resources","election_data.csv")
output_path = os.path.join(cpath,"PyPoll","Analysis","election_results.txt")

# Check if file exists 
if not(os.path.exists(csvpath)):
    print("\n\nFile Not Found")

# Open the file in read only mode and preform analyis
with open(csvpath,'r') as csvfile:

    votes= {} # Create a dictornary for vote count
    
    totalVotes= 0 # Count the total number of Votes cast

    # Set the CSV file to a vaiable with a delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader) # Read and store the CSV Header

    for (ballot_ID,County,Candidate) in csvreader:
        totalVotes += 1 # increment the number of votes

        if (Candidate in votes):
            # if the Candidate Exists, count the votes
            votes[Candidate] += 1 
        else:
            # if the Candidate Exists, Update the list and count the Votes
            votes[Candidate] = 1

### ----------- Print to Terminal and File Election Results --------------

# Create a Temporary Winner with No name and Zero Votes
WinnerVotes = 0
Winner = "" 

# Print Header and write to file, Command are listed together to be able to change easier

with open(output_path,'w') as output_text:
    print(f"\nElection Results \n----------------------------")
    output_text.write(f"\nElection Results \n----------------------------")

    # Print the total number of votes
    print(f"\nTotal Votes: {totalVotes:,}\n--------------------\n")
    output_text.write(f"\nTotal Votes: {totalVotes:,}\n--------------------\n")

    # Go though each candidate and print the percentage of votes with absolute number of votes
    for Candidate in votes:
        print(f"{Candidate} : {votes[Candidate]/totalVotes:.3%} ({votes[Candidate]:,})")
        output_text.write(f"{Candidate} : {votes[Candidate]/totalVotes:.3%} ({votes[Candidate]:,})\n")

        if WinnerVotes < votes[Candidate]:
            # if the candidate has more votes then the perious temporary winner, they are the new temporary winner
            WinnerVotes = votes[Candidate]
            Winner = Candidate

    print(f"-------------------------\nWinner: {Winner} \n-------------------------")
    output_text.write(f"-------------------------\nWinner: {Winner} \n-------------------------")

###### Sources:

# String Formating (https://docs.python.org/3/library/string.html#format-string-syntax)
# Wite Command (https://docs.python.org/3/library/io.html#io.TextIOBase.write)
# Thousand Sperator (https://stackoverflow.com/questions/1823058/how-to-print-a-number-using-commas-as-thousands-separators)
