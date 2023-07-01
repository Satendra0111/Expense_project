

    
file=open(".\expense\Demo.csv", "r")  # open file
data= file.readline()                 # readline 
while data != "":
    data = file.readline()
    line= data.split(",")
    if line[0]=="tom":             # Actual Filter Happening
        print(line)
 