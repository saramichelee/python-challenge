import csv

csvname = "budget_data.csv"

with open(csvname, newline="") as budgetcsv:
    csv_reader = csv.reader(budgetcsv, delimiter = ",")

    # header is present
    csv_header = next(csv_reader)
    
    changes = []

    current_revenue = 0
    previous_revenue = 867884

    # count net total amount for all months
    netTotal = 0
    month_count = 0
    tempmax = {}
    tempmin = {}

    for row in csv_reader:
        netTotal += int(row[1])
        month_count += 1
        current_revenue = row[1]
        change = int(current_revenue) - int(previous_revenue)
        changes.append(change)
        previous_revenue = current_revenue 
        

        if change > 0 :
            tempmax.update({row[0]:change})
        elif change < 0:
            tempmin.update({row[0]:change})

    datelist = csv.writer()
    #pop indexs
    max_change = max(int(a[1]) for a in tempmax)
    min_change = min(int(i[1]) for i in tempmin)

    print(maxchange)
    print(minchange)
    
        
    #average of all the revenue changes  
    averagechange = sum(changes)/month_count

    #netTotal = sum(float(m[1]) for m in csv_reader)
    print(netTotal)
    
    # count of rows (i.e. total months)
    print(month_count)



    #averageChange = netTotal/month_count
    print(averagechange)



