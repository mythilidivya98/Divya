n,k=map(int,input().split())
n1=list(map(int,input().split()))
sum=0
for i in range(len(n1)-1):
    for j in range(i+1,len(n1)):
        if(n1[i]+n1[j]==k):
           print("yes")
