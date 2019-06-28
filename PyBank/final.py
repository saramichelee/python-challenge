import csv

csvname = "budget_data.csv"

with open(csvname, newline="") as budgetcsv:
    csv_reader = csv.reader(budgetcsv, delimiter = ",")

    # header is present
    csv_header = next(csv_reader)

    # variables in for loop set in global scope
    month_count = 0
    current_revenue = 0
    previous_revenue = 867884

    # empty lists created
    changes = []
    months = []
    prolos = []

    for row in csv_reader:
        month_count += 1
        current_revenue = row[1]
        month = str(row[0])
        prolo = int(row[1])
        change = int(current_revenue) - int(previous_revenue)

        months.append(month)
        prolos.append(prolo)
        changes.append(change)

        previous_revenue = current_revenue

    #print(month_count)

    netTotal = sum(prolos)
    #print(netTotal)

    totalChanges = sum(changes)
    averageChanges = round(totalChanges/(month_count-1),2)
    #print(averageChanges)

    maxProfit = max(changes)  #max value
    maxIndex = changes.index(maxProfit)  #month index
    maxMonth = months[maxIndex]  #month value max
    #print(maxProfit)
    #print(maxMonth)

    minLoss = min(changes)  #min value
    minIndex = changes.index(minLoss)  #month index
    minMonth = months[minIndex]  #month value min
    #print(minLoss)
    #print(minMonth)

    print("Financial Analysis")
    print("-----------------------")
    print("Total Months: " + str(month_count))
    print("Total: $" + str(netTotal))
    print("Average Change: $" + str(averageChanges))
    print("Greatest Increase in Profits: " + maxMonth + " ($" + str(maxProfit) + ")")
    print("Greatest Decrease in Profits: " + minMonth + " ($" + str(minLoss) + ")")