n = int(input())
rst = []
for _ in range(n):
    rst.append(int(input()))

rst.sort(reverse=True)

for i in rst:
    print(i, end=' ')