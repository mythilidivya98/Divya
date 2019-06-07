n1,k=map(int,input().split())
n2=list(map(int,input().split()))
c=0
for i in range(len(n2)):
    if n2[i]==k:
        c=c+1
print(c)
