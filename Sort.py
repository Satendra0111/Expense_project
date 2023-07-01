file=open(".\expense\Demo.csv", "r")  # open file
data= file.readline()  # readline 
sortData=[]
while data != "":
    data = file.readline()
    line= data.split(",")
    sortData=int(line[2]).sort()    
print(sortData)