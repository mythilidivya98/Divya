S1=input()
a=b=0;
for i in S1:
    if i.isalpha():
        b+=1 
    elif i.isnumeric():
        a+=1 
if(a>=1 and b>=1):
    print("Yes")
else:
    print("No")
