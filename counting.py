st=input()
st1=len(st)
v=[]
k=0
for i in range(0,st1):
    c=int(st[i])**st1
    v.append(c)
for i in range(0,int(len(v))):
   k=k+v[i]
print(k)
    
