def expenseCreation():
    date = input("please enter date: ")
    category = input("please enter category: ")
    discreption = input("please enter discreption: ")
    amount = input("please enter amount: ")
    return date, category, discreption, amount



def writeExpenseCreation(date, category, discreption, amount):
    file = open('expenseDetails.csv', 'a')
    if file.tell() == 0:
        file.write("date, category, discreption, amount\n")

    print("expense report saved successfully!")


def getexpenseDataFromCSV(student_name):
    with open('expenseDetails.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row
        for row in reader:
            date, category, discreption, amount = row
        

flag = "y"
while flag == "y":
    date, category, discreption, amount = expenseCreation()
    writeExpenseCreation(date, category, discreption, amount)

    flag = input("Do you want to add more data (y/n): ")