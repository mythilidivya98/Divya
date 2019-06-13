num=input()
count=1
for i in range(len(num)-1):
    a=num[i]+num[i+1]
    b=int(a)
    if b<=26 and num[i]!="0":
        count+=1
if count==3:
    print(count)
else:
    print(count+(count-1)//2)
