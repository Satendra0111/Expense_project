

# Filter the data by category

def catfilters(category): 
    
    file=open(".\expense\Demo.csv", "r")  # open file
    data= file.readline()                 # readline 
    while data != "":
        data = file.readline()
        line= data.split(",")
        if line[0]==category:             # Actual Filter Happening
            print(line)
    
