import random

#without using dictionary

cnt=[]
cnt=[0]*26
with open('intro.txt','r') as f:
    for line in f:
        for word in line.split():
         #  print(word)
           x=random.choice(word)
           print(x)
           for i in range(0,25):
               if(x==chr(65+i) or x==chr(97+i)):
                   cnt[i]=cnt[i]+1
f1=open('app.csv','w')
for i in range(0,25):
    f1.write("%c = " % chr(65+i))
    f1.write("%d \t" % cnt[i])
   # f1.print(chr(65+i)," = ",cnt[i])
f.close()
f1.close()

