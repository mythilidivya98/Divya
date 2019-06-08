n1=int(input())
n2=list(input().split())
r=sorted(n2)
t=reversed(r)
if(t!=0):
    print(' '.join(t))
else:
    print("0")
