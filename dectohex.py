n=int(input())
while(n!=0):
    b=n%16
    n=n//16
    g={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',16:'G'}
    if(b<10):
        print(b,end=" ")
    else:
        print(g[b],end=" ")
