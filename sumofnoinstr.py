a=input()
b=[]
sum=0
for i in a:
    if i.isdigit():
        c=i
        b.append(c)
k=len(b)
for i in range(k):
    sum=sum+int(b[i])
print(sum)
