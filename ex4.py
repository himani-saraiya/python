r = [1, 2, 3, 7, 5, 6, 8, 9];
i=0
p=1
while i<len(r):
    if r[i]%2==0:
        p=p*r[i]
    i+=1
print(p)