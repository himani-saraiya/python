# arr = [1, 2, 3, 58, 5, 6, 62, 8, 70]
# sum=0
# i=0
# while i<len(arr):
#     if arr[i]>50:
#         sum+=arr[i]
#     i=i+1
# print(sum)

a=[2,4,5,1,6,6,5,4,7,1,8]
i=0
b=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i=i+1
b.sort()
print(b)

