import csv
def add(d1,key,value):
    d1[key]=value


xx=1
yy=1
with open("MAINDATA.csv",mode='r') as csvfile :     
    current=list(csv.reader(csvfile))                 #gotta call specfic plant csv
    csvfile.close()
    row=len(current)-1
    xx=int(current[row][3])
    yy=int(current[row][4])
    print(int(xx),int(yy))

aa="SPLIT"+str(xx)+str(yy)+".csv"
with open(aa,mode='r') as csvfile :     #feeding each values to csv
    data=list(csv.reader(csvfile))                 #gotta call specfic plant csv
    csvfile.close()


for i in range (0,len(data)):
    for j in range (0,6):
        data[i][j]=float(data[i][j])
for o in data:
    if o[5]<4:
        data.remove(o)
tem=[]
d=[]
hum=[]
humdi={}
tempdi={}
for a in data:       
    tem.append(a[0])    
tem=list(set(tem))
for k in range (len(tem)):
    s=tem[k]
    i=0
    hum=[]
    for i in range (len(data)):
        if s==data[i][0]:
            hum.append(data[i][1])
    hum=list(set(hum))
    j=0
    for j in range (len(data)):
        if s==data[j][0]:
            humdi={}            
            c=0
            for z in range (len(hum)):
                d=[]
                for b in range (len(data)):
                    if s==data[b][0] and hum[z]==data[b][1]:
                        d.append(data[b][2])                    
                c=len(d)
                y=sum(d)/c
                add(humdi,hum[z],y)
        add(tempdi,s,humdi)
print(tempdi)



