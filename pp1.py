import math
in=int(input())
string=math.log10(in)/math.log10(2)
if math.ceil(string)==math.floor(string):
  print("0")
else:
  c=(in-1)//2
  string=c*2
  print(in-string)
