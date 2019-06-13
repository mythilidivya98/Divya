n=int(input())
n2=list(input().split())
e=[]

for i in range(n):
    for j in range(i+1,n):
        if (n2[i]==n2[j] and n2[i] not in e):
            k=n2[i]
            e.append(k)
            break
else:
    print("unique")
print(' '.join(e))
