import csv
def qread():
    with open("SPLIT11.csv",mode='r') as csvfile :     #feeding each values to csv
        data=list(csv.reader(csvfile))
        row=len(data) 
        a=data[row-2][0]
        
        print(row)
        print(data[0][0][1])
        csvfile.close()
        print("done")
        
qread()