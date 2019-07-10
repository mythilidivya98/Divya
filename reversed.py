t=int(input())
for i in range(0,t):
    n=int(input())
    b = [int(i) for i in input().split()]
    b.reverse()
    for i in b:
        print(i, end = " ")
    print()
