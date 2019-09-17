s1=input()
a=[]
b=[]
for i in range(0,len(s1)):
    if(i%2==0):
        a.append(s1[i])
    else:
        b.append(s1[i])
print("".join(a),"".join(b))
