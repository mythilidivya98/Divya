n1=int(input())
n2=list(input().split())
e=[]
#c=0
for i in range(n1):
    for j in range(i+1,n1):
        if (n2[i]==n2[j] and n2[i] not in e):
            k=n2[i]
            e.append(k)
            break
else:
    print("unique")
print(' '.join(e))
