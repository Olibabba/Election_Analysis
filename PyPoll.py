import datetime

now = datetime.datetime.now()
print(f'The current time is {now}')

# Add our dependencies
import csv
import os


#A ssign a variable for the file to load and the path.
file_to_load =  os.path.join('Resources', 'election_results.csv')
# Assign a variable to the file to a path.
file_to_save = os.path.join('analysis', 'election_analysis.txt')

#open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #to do: perform analysis
    #print(election_data)
    for headers in next(next(file_reader)):
        print(headers)

#using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:

# Write some data to the file
    txt_file.write(f"Counties in the Election\n---------------------\nArapahoe \nDenver \nJefferson \n-- time of last edit {now}--")



    #Find Total number of votes cast
    #Make A complete list of candidates who received votes
    #Find Total number of votes each candidate received
    #Calculate Percentage of votes each candidate won
    #Declare The winner of the election based on popular vote


# Dead Code
    #election_data = open(file_to_load, 'r')

    #Close the file.
    #election_data.close()

    # Close the file
    #outfile.close()