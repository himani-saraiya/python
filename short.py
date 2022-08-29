# a=[2,4,5,1,6,6,5,4,7,1,8]
# i=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     b.short()
# print(b)

a=[1,2,3,4,5]
b=[6,3,4,9]
i=0
while i<len(b):
    if b[i] not in a:
        a.append(b[i])
    i=i+1
print(a)