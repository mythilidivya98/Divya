a=input()
b=[]
c=[]
for i in range(0,len(a)):
    if(i%2!=0):
        b.append(a[i])
    else:
        c.append(a[i])
k=b+c[::-1]
print("".join(k))
