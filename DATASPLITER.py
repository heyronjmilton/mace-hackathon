import csv

data1=[]
with open("MAINDATA.csv",mode='r') as csvfile :     #feeding each values to csv
    data=list(csv.reader(csvfile))
    csvfile.close()


def put1 (a):
    aa="SPLIT"+str(a[3])+str(a[4])+".csv"
    with open(aa,mode='a',newline="") as csvfile :     #feeding each values to csv
        mywriter=csv.writer(csvfile)
        mywriter.writerows([a]) 
        csvfile.close()
    print("done")


for i in range (0,len(data)):
    for j in range (0,6):
        data[i][j]=int(data[i][j])
x=3
y=3
for a in data:
    for c in range (0,x+1):
        for b in range (0,y+1):
            if a[3]==c and a[4]==b:
                put1(a)
        print(data1)
    print(" ")