def large(a,n)
  min=a[0]
  for i in range(1,n):
      if a[i]<min:
         min=a[i]
  return min
  a=[]
  n=len(a)
  ans=large(a,n)
  print(ans)
