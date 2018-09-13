import random
import csv
import re
d={}
with open('app.csv','w') as csv_file:
    h = ['letter', 'count']
    h1 = csv.DictWriter(csv_file, fieldnames=h)
    h1.writeheader()
    f=open('intro.txt','r')
    for line in f:
        for w in line.split():
           print(w)
           x=random.choice(w)
           print(x)
           if(x in d):
               d[x]=d.get(x)+w.count(x)
           else:
               d[x]=w.count(x)
          #  print(x,w.count(x))
    print(d)
    for i in range(0,25):
        fg=1
        for y in d:
            if(y==chr(97+i) or y==chr(65+i)):  #both upper case or lower case
                h1.writerow({'letter':chr(97+i),'count':d[y]})
                fg=0
        if(fg==1):
            h1.writerow({'letter':chr(97+i),'count':'0'})
f.close()

