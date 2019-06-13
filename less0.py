n=int(input())
l1=list(map(int,input().split()))
mi=max(l1)
a,b=0,0
for i in range(0,len(l1)-1):
  for j in range(i+1,len(l1)):
    if abs(l1[i]+l1[j])<mi:
      a,b=l1[i],l1[j]
      mi=abs(a+b)
print(a,b)
