a=input().split()
ln=[]
for i in a:
  ln.append(i[::-1])
print(*ln,sep=' ')
