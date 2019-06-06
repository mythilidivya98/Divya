a1=int(input())
n1=list(input().split())
sum=0
for i in range(a1):
    sum=sum+int(n1[i])
d=len(n1)
d1=sum//d
print(d1)
