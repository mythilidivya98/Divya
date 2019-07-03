a=input()
b=[]
c=[]
for i in range(0,len(a)):
    if(i%2==0):
        b.append(a[i])
    else:
        c.append(a[i])
for i in range(len(b)):
    for j in range(int(c[i])):
        print(b[i],end=" ")
