k, n = map(int, input().split())
lst = list(int(input()) for _ in range(k))
start, end = 1, max(lst)

while start <= end:
    mid = (end+start) // 2
    rst = 0
    for i in lst:
        rst += i//mid
    if rst >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)