n, m = map(int, input().split())
lst = list(int(input()) for i in range(n))

start, end = 1, max(lst)

while start <= end:
    mid = (start + end) // 2
    rst = 0

    for i in lst:
        rst += i // mid

    if rst >= m:
        ans = mid
        start = mid +1
    else:
        end = mid - 1

print(ans)