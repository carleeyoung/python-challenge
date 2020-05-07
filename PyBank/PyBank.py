import os
import csv

csvPath = os.path.join("../Resources", "budget_data.csv")

months = 0
netProfit = 0
previousProfit = 867884 
change_dict = {}
sum = 0
greatest_increase = 0
greatest_decrease = 0


with open(csvPath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)
    
    for row in csvreader:
        
        #calculate the total number of months
        months = months + 1
        
        #net total amount of "Profit/Losses" over the entire period
        profit = int(row[1])
       
        netProfit = netProfit + profit
        
        #changes in profit
        profitChange = profit - previousProfit
        
        month = row[0]

        #add month: change in profit to dictionary
        change_dict[month] = profitChange

        #set value for previous profit        
        previousProfit = int(row[1])
        

for month in change_dict:
    #calculate sum of profit/losses change to be used in average calculation
    sum = sum + change_dict[month]

    #find greatest increase in profit
    if change_dict[month] > greatest_increase:

            greatest_increase = change_dict[month]
            greatest_increase_month = month

    #find greastest decrease in profit
    if change_dict[month] < greatest_decrease:

            greatest_decrease = change_dict[month]
            greatest_decrease_month = month

#find the average change in profit
averageChange = sum / len(change_dict)


print("Financial Analysis")

print("------------------------------------")    

print(f"Total Months: {months}")

print(f"Total: ${netProfit}")

print(f"Average Change: ${round(averageChange, 2)}")

print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")

print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")


#Write results summary in a .txt file
output_path = os.path.join("../Analysis", "PyBank.txt")

Summary = ["Financial Analysis", "------------------------------------", f"Total Months: {months}", f"Total: ${netProfit}", f"Average Change: ${round(averageChange, 2)}", f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})", f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})"]  

with open(output_path,"w") as PyBank_text:
   
    PyBank_text.write('\n'.join(Summary))

