import sys, string, math
s,s1 = input().split()
m1 = len(s)
m2 = len(s1)
if m2 > m1 :
    j = 0
    while j<m1 and s[j] == s1[j] :
        j += 1
    print(m2-j)
elif m2 == m1 :
    j = 0
    while j<m2 and s[j] == s1[j] :
        j += 1
    print(m2-j)
else :
    j = 0
    while j<m2 and s[j] == s1[j] :
        j += 1
    s31 = s[j:]
    s32 = s1[j:]
    L = list(s31)
    k = 0
    for c in s32 :
        if c in L :
            k += 1
            L.remove(c)
    print(m1-j-k)
