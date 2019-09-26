a=input()
b=""
for i in a:
    if(i.lower()!="z"):
        b+=chr(ord(i)+1)
    else:
        if(i=="z"):
            b+='a'
        else:
            b+='A'
print(b)
