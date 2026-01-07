n = int(input())
lst = []

for i in range(n):
    a, b = input().split()
    lst.append((a, int(b)))

lst = sorted(lst, key=lambda x:x[1])

for i in lst:
    print(i[0], end=' ')
