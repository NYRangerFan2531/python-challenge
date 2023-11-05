# Rutgers Data Boot Camp Module 3 Challange
# Leonid Lyakhovich

# Part 1: Py Bank

# import statments
import os, csv

cpath = os.getcwd()


# Set Path of CSV file
csvpath = os.path.join(cpath,"PyBank","Resources","budget_data.csv")
output_path = os.path.join(cpath,"PyBank","Analysis","output.txt")

# Check if file exists 
if not(os.path.exists(csvpath)):
    print("\n\nFile Not Found")

# Open the file in read only mode and preform analyis
with open(csvpath,'r') as csvfile:

    # Set the CSV file to a vaiable with a delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader) # Read and store the CSV Header

    # Initialize Variables as First Months Values
    (date,monReturntext) = next(csvreader)
    nmonths = 1 # Set the Number of Months to 1 as First Month of data is read
    totalchangeProfit =0 # Set the Total Change in profits to Zero to start
    monReturn = int(monReturntext) # Cast the monthly return from text to interger

    # Set the statistics of the program to the first month's data
    total= monReturn
    maxInc=monReturn
    maxIncDate = date
    maxDec=monReturn
    maxDecDate=date
    previousmonReturn=monReturn

    for (date,monReturntext) in csvreader:
        # Read in the next month

        nmonths+=1 # increment the number of months
        monReturn = int(monReturntext) # Cast the monthly return from text to interger

        # Add the Monthly Return to the total
        total+=monReturn

        # Calulate the Change in Profits from the Previous Month
        changeProfit = monReturn - previousmonReturn

        # add the change in profits to the total
        totalchangeProfit += changeProfit
        
        if changeProfit>maxInc:
            # If this months increase is greater than previous max increase, document the increase and the month
            maxInc = changeProfit
            maxIncDate = date
        elif changeProfit<maxDec:
            # If this months decrease is greater than previous max Decrease, document the decrease and the month
            maxDec = changeProfit
            maxDecDate = date

        # set up for next itiration by seting this months' return to last months return
        previousmonReturn=monReturn

# Print Report to the Terminal
print("\nFinancial Analysis \n--------------------------------")

print(f"\nTotal Months: {nmonths}")
print(f"\nTotal: ${total:,.2f}")
print(f"\nAverage Change: ${totalchangeProfit/(nmonths-1):,.2f}") #For average Change, Number of Months is one less than given 

print(f"\nGreatest Increase in Profits: {maxIncDate} (${maxInc:,})")
print(f"\nGreatest Decrease in Profits: {maxDecDate} (${maxDec:,})")

# Output Report to Text File
with open(output_path,'w') as textfile:

    textfile.write(f"\nFinancial Analysis \n--------------------------------")
    textfile.write(f"\nTotal Months: {nmonths}")
    textfile.write(f"\nTotal: ${total:,.2f}")
    textfile.write(f"\nAverage Change: ${totalchangeProfit/(nmonths-1):,.2f}")

    textfile.write(f"\nGreatest Increase in Profits: {maxIncDate} (${maxInc:,})")
    textfile.write(f"\nGreatest Decrease in Profits: {maxDecDate} (${maxDec:,})")


###### Sources:

# String Formating (https://docs.python.org/3/library/string.html#format-string-syntax)
# Wite Command (https://docs.python.org/3/library/io.html#io.TextIOBase.write)
# Thousand Sperator (https://stackoverflow.com/questions/1823058/how-to-print-a-number-using-commas-as-thousands-separators)