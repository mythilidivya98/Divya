n=int(input())
a1=input()
k=""
b=[]
for i in range(0,n-1):
  s=input()
  for j in range(1,len(a1)):
    if(a1[0:j] in s ):
      k=a1[0:j]
  b.append(k)
  k=""
m=b
count=0
for g in b:
    m.remove(g)
    for l in m:
        if(g in l):
            count=count+1
    if(count>=n//2):
        ans=g
    m=b
    count=0
print(ans)
