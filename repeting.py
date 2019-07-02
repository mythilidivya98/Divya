n=int(input())
b=input().split()
l1=[]
l2=[]
for i in range(n):
    l1.append(b[i])
for i in range(n):
    for j in range(i+1,n):
        if(l1[i]==l1[j] and i!=j ):
            m=l1[i]
            l2.append(m)
m=set(l1)       
print(' '.join(m))
print(' '.join(l2))
