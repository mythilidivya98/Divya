a=input()
b=[]
c=[]
for i in range(0,len(a)):
    if(i%2==0):
        b.append(a[i])
    else:
        c.append(a[i])
for i in range(int(c[0])):
        print(b[0],end=" ")
for i in range(int(c[1])):
        print(b[1],end=" ")
