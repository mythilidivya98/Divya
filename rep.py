n,k=map(int,input().split())
n1=list(map(int,input().split()))
for i in range(len(n1)):
    if n1[i]==k:
        print("yes")
        break
else:
    print("no")
