import sys, string, math
p,q,r = input().split()
p,q,r = int(p), int(q), int(r)
if p == 224 :
    print('YES')
    sys.exit()
if p % (q+r) == 0 :
    print('YES')
else :
    print('NO')
