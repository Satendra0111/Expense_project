

def amountfilters(amount): 
    
    amount = int(amount)
    file=open(".\Expense_project\expenseDetails.csv", "r")  # open file
    data= file.readline()                 # readline 
    while data !="":
        data = file.readline()
        line = data.split(",")
        if line[3]==amount:             # Actual Filter Happening
            print(line)
            