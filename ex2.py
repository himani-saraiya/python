a=["eat","sleep","repeat","code"]
i=0
b=[]
while i<len(a):
    if len(a[i])>5:
        b.append(a[i])
    i=i+1
print(b)