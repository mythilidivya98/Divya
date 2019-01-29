def large(a,n)
  max=a[0]
  for i in range(1,n):
      if a[i]>max:
         max=a[i]
  return max
a=[]
n=len(a)
ans=large(a,n)
print(ans)
