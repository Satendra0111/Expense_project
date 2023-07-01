
##Using while loop##

def expenseList(filename):
    print("*********Here all expense details **************")
    file= open(filename, "r")
    while(True):
        data = file.readline()
        print(data)
        if not data:
            break
expenseList("expenseDetails.csv")