a1=int(input())
b1=[int(i) for i in input().split()]
x=0
for i in range(a1):
   for j in range(i):
      if b1[j]<b1[i]:
         x+=b1[j]
print(x)         
