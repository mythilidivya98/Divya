n=int(input())
l=list(map(int,input().split()))
op=[]
for i in range(0,len(l)-2):
  for j in range(i+1,len(l)-1):
    for k in range(j+1,len(l)):
      if l[i]+l[j]==l[k]:
        op.append([l[i],l[j],l[k]])
for i in op:
  print(*i)
