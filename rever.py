st=input().split()
b=[]
for i in range(0,len(st)):
    t=st[i][::-1]
    b.append(t)
print(" ".join(b))
