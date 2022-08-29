# n = int(input())
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input()
# print(scores)

i=0
while i<=5:
    j=0
    while j<i:
        print(j,end="")
        j=j+1
    i=i+1
print(i,end="")