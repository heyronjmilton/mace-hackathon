import csv
import random as r


count=10000  #hundred codes
X=3       #no of row of plant
Y=3       #no of col of plant
for a in range (0,count):
    temp=r.randint(28,35)
    hum=r.randint(65,85)         #giving random values in range for simulation
    moist=r.randint(80,90)
    xcr=r.randint(1,X)
    ycr=r.randint(1,Y)
    qindex=r.randint(1,5)
    data=[temp,hum,moist,xcr,ycr,qindex]


    with open("MAINDATA.csv",mode='a',newline="") as csvfile :     #feeding each values to csv
        mywriter=csv.writer(csvfile)
        mywriter.writerow(data) 
        csvfile.close()
        print("done")
        
