l1=int(input())
arr=list(map(int,input().split()))
for i in range(0,len(arr)):
    if(arr[i]%2==0 and i%2!=0):
        print(arr[i],end=" ")
    elif(arr[i]%2!=0 and i%2==0):
        print(arr[i],end=" ")
