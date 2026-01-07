n = int(input())
lst = list(map(int, input().split()))
x = int(input())

lst.sort()
cnt = 0
left, right = 0, n-1


while left < right:
    s = lst[left] + lst[right]

    if s == x:
        cnt += 1
        left += 1
        right -= 1
    elif s < x :
        left += 1
    else:
        right -= 1

print(cnt)