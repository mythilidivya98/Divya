import math
a1=int(input())
b1=math.log10(a1)/math.log10(2)
if math.ceil(b1)==math.floor(b1):
	print(0)
else:
	c=(a1-1)//2
	d=c*2
	print(a1-d)
