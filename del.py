inp,inp2=input().split()
temp=0
if len(inp)>len(inp2):
  inp,inp2=inp2,inp
i=0
while i<len(inp):
  temp+=(ord(inp2[i])-ord(inp[i]))
  i+=1
for i in range(i,len(inp2)):
  temp+=ord(inp2[i])-ord('a')+1
print(temp)
