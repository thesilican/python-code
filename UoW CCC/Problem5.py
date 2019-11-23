import math

triangle = []
inputs = input().split()
triangle_size = int(inputs[0])
sub_triangle_size = int(inputs[1])
for i in range(triangle_size):
    l = []
    for j in input().split():
        l.append(int(j))
    triangle.append(l)
triangle_heads_size = triangle_size - sub_triangle_size + 1

triangleSums = []
for i in range(triangle_heads_size):
    l = []
    for j in range(i + 1):
        l.append(None)
    triangleSums.append(l)

for i in range(triangle_size):
    for j in range(i + 1):
        num = triangle[i][j]
        for x in range(sub_triangle_size):
            for y in range(x + 1):
                if i - x < 0 or j - y < 0:
                    continue
                if triangleSums[i - x][j - y] == None or num > triangleSums[i - x][j - y]:
                    triangleSums[i - x][j - y] = num

acc = 0
for i in triangleSums:
    for j in i:
        acc += j;
print (acc)





















# 

# the_sum = 0

# for i in range(triangle_heads_size):
#     for j in range(i + 1):
#         m = 0
#         for x in range(sub_triangle_size):
#             for y in range(x + 1):
#                 n = triangle[i + x][j + y]
#                 if n > m:
#                     m = n
#         the_sum += m
# print(the_sum)
