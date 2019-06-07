n=int(input())
n2=list(input().split())
f=[]
#c=0
for i in range(n):
    for j in range(i+1,n):
        if (n2[i]==n2[j] and n2[i] not in f):
            k=n2[i]
            f.append(k)
print(' '.join(f))
