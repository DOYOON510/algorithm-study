# n, m = map(int, input().split())
# lst = list(map(int, input().split()))
# rst = 0
# for i in range(n):
#     for j in range(i+1,n):
#         if lst[i] != lst[j]:
#             rst += 1
#
# print(rst)

n, m = map(int, input().split())
lst = list(map(int, input().split()))
rst = 0
array=[0]*11

for x in lst:
    array[x]+=1

for i in range(1, m+1):
    n -= array[i]
    rst += array[i]*n

print(rst)