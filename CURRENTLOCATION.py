import csv
import random as r
import time
import CURRENTCSVSPLITTER,motorread

def qread():
    with open("QINDEX.csv",mode='r') as csvfile :     #feeding each values to csv
        data=list(csv.reader(csvfile))
        row=len(data) 
        a=data[row-2][0]
        
        print(row)
        csvfile.close()
        print("done")
        return a


def put1 (temp,hum,moist,crx,cry,qindex,motorstate):
    with open("CURRENT.csv",mode='a',newline="") as csvfile :     #feeding each values to csv
        mywriter=csv.writer(csvfile)
        mywriter.writerow([temp,hum,moist,crx,cry,qindex,motorstate]) 
        csvfile.close()
        print("done")


x=1
y=1


while(1):
    
    con=0
    with open("condition.csv",mode='r') as csvfile:
        data=list(csv.reader(csvfile))
        con1=int(data[0][0])
        con=con1
        
    if con==0:
        for a in range (1,4):
            for b in range (1,4):
                temp=r.randint(28,30)
                hum=r.randint(75,80)
                moist=r.randint(80,90)
                qindex=qread()

                crx=a
                cry=b
                motorstate=motorread.motorstate()
                time.sleep(3)
                put1(temp,hum,moist,crx,cry,qindex,motorstate)
                CURRENTCSVSPLITTER.do()

                
        

    if con==1:
        with open("value.csv",mode='r') as csvfile:
            data=list(csv.reader(csvfile))
            a=int(data[0][0])
        if a==1:
            a=1
            b=1
        if a==2:
            a=1
            b=2
        if a==3:
            a=1
            b=3
        if a==4:
            a=2
            b=1
        if a==5:
            a=2
            b=2
        if a==6:
            a=2
            b=3
        if a==7:
            a=3
            b=1
        if a==8:
            a=3
            b=2
        if a==9:
            a=3
            b=3    
        temp=r.randint(28,30)
        hum=r.randint(75,80)
        moist=r.randint(80,90)
        
        crx=a
        cry=b
        
        time.sleep(7)
        motorstate=motorread.motorstate()
        put1(temp,hum,moist,crx,cry,qindex,motorstate)
        CURRENTCSVSPLITTER.do()
