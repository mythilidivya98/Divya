from itertools import combinations
string1,n1=map(int,input().split())
n=len(str(string1))
a=list(combinations(str(string1),n-n1))
a=(sorted(a))
b1="".join(a[0])
print(b1)
