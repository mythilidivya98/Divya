import math
import functools
in1,in2=map(int,input().split())
list=[int(i) for i in input().split()]
for i in range(in2):
   c,d=map(int,input().split())
   temp=functools.reduce(math.gcd,list[c-1:d])
   print(temp)
