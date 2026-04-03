n = int(input())
lst = list(map(int, input().split()))
lst.sort()
cnt = 0

for i in range(n):
    l = 0
    r = n - 1
    while l < r:
        sum_num = lst[l] + lst[r]
        if sum_num == lst[i]:
            if i != l and i != r:
                cnt += 1
                break
            elif i == l:
                l += 1
            elif i == r:
                r -= 1
        elif sum_num < lst[i]:
            l += 1
        elif sum_num > lst[i]:
            r -= 1

print(cnt)
