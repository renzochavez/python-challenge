import csv

csvpath_output = ("main.txt")

row_count=0
total_sum=0
total_list_changes= []
largest_increase=["",0]
largest_decrease=["",999999]

with open('Resources/budget_data.csv', 'r') as budget_csv:
    csv_reader = csv.reader(budget_csv, delimiter=',')
    header = next(csv_reader)
    first_row = next(csv_reader)
    lastmonth_change = int(first_row[1])
    total_sum+= int(first_row[1])
    row_count+=row_count+1

    for row in csv_reader:
        
        total_change = int(row[1]) - lastmonth_change
        if total_change > largest_increase[1]:
            largest_increase[1] = total_change
            largest_increase[0] = row[0]
        if total_change < largest_decrease[1]:
            largest_decrease[1] = total_change
            largest_decrease[0] = row[0]  
        total_list_changes.append(int(row[1]))
        #largest_increase=max(largest_increase,total_change)
       # largest_decrease=min(largest_decrease,total_change)
        row_count+= 1
        total_sum+= int(row[1])
        lastmonth_change = int(row[1]) 
        
        
monthly_avg = sum(total_list_changes)/len(total_list_changes)    

print('Financial Analysis')
print('----------------------------')
print(f"Total Months: {row_count}")
print(f"Total: ${total_sum}")
print(f"Average Change: ${monthly_avg}")
print(f"Greatest Increase in Profits: {largest_increase[0]} (${largest_increase[1]})") 
print(f"Greatest Decrease in Profits: {largest_decrease[0]} (${largest_decrease[1]})")  

with open(csvpath_output, "w") as txt_file:
    txt_file.write("Total Months: " + str(row_count))
    txt_file.write("\n")
    txt_file.write("Total: " + "$" + str(total_sum))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(monthly_avg,2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(largest_increase[0]) + " ($" + str(largest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(largest_decrease[0]) + " ($" + str(largest_decrease[1]) + ")")