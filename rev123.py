g,h=map(int,input().split())
m=list(map(int,input().split()))
n=[]
for i in range(0,len(m)):
    if(h<m[i]):
        d=m[i]-h
        n.append(d)
    else:
        e=m[i]-h
        n.append(e)
print(sorted(n))
