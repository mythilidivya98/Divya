n1=int(input())
a1=list(map(int,input().split()))
b=sorted(a1)[::-1]
c=""
if(a1==[0]*n1):
    print("0")
else:
    for i in b:
        c=c+str(i)
    print(int(c))   
