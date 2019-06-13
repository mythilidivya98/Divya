n=int(input())
a1=list(map(int,input().split()))
c=[]
count=0
for i in a1:
  if i not in c:
    c.append(i)
for j in c:
  for k in a1:
    if(j==k):
      count=count+1
  if(count==1):
    print(j)
  count=0
