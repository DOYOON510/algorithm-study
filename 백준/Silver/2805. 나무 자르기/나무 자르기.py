n, m = map(int, input().split())
lst = list(map(int, input().split()))
start, end = 1, max(lst)

while start <= end:
    mid = (end+start) // 2
    rst = 0
    for i in lst:
        if i >= mid :
            rst += (i-mid)
    if rst >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)