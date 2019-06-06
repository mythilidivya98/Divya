r1=int(input())
a=list(input().split())
b1=0
for i in range(r1):
    if(int(a[i])>0):
        b=sorted(a)
        b1=1
    else:
        c=reversed(a)
if(b1==1):
    print(' '.join(b))
else:
    print(' '.join(c))
