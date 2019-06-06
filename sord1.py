r21=int(input())
a=list(input().split())
b11=0
for i in range(r21):
    if(int(a[i])>0):
        b=sorted(a)
        b11=1
    else:
        c=reversed(a)
if(b11==1):
    print(' '.join(b))
else:
    print(' '.join(c))
