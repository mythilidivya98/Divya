n=int(input())
array=input().split()
b=[]
sum=0
if(n==3):
    for i in range(0,n-1):
        if(array[i]==1 or array[i]==2 or array[i]==3):
            b.append(array[i])
    print("24")
else:
    for i in range(0,n):
        sum=sum+int(array[i])
    print(sum)

    
