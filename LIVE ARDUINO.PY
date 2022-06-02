from random import randint
import serial
import csv
import sys

if __name__ == '__main__':

    ser = serial.Serial('COM3', 9600, timeout=1)
    ser.reset_input_buffer()
    f=open("QINDEX.csv",'r')
  
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            x=line.split(",")
            a=int(x[0])
            b=int(x[1])
            c=int(x[2])
            with open("QINDEX.csv") as csvfile:
                data=list(csv.reader(csvfile))
                d=int(data[0][0])
                            


                fields=["HUMIDITY","TEMPERATURE","MOISTURE","X AXIS","Y AXIS","CONDITION"]
                with open("section_coordinate.csv") as csvfile:
                    data1=list(csv.reader(csvfile))
                    d1=int(data1[0][0])
                    print(d1)

                if d1==1:    
                    xx=1
                    yy=1

                if d1==2:    
                    xx=1
                    yy=2

                if d1==3:    
                    xx=1
                    yy=3

                if d1==4:    
                    xx=2
                    yy=1

                if d1==5:    
                    xx=2
                    yy=2

                if d1==6:    
                    xx=2
                    yy=3
            
                if d1==7:    
                    xx=3
                    yy=1

                if d1==8:    
                    xx=3
                    yy=2

                if d1==9:    
                    xx=3
                    yy=3
                with open("MAINDATA.csv",'a', newline='') as f1:
                    csv.writer(f1).writerow([a,b,c,xx,yy,d])
                    f.close()