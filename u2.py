from collections import *
a1 = int(input())
b1 = [int(i) for i in input().split(' ')]
d = defaultdict(int)

found = False
for i in range(a1):
    d[b1[i]] += 1
    if d[b1[i]] == 2:
        print(b1[i])
        found = True
if not found:
    print("unique")
