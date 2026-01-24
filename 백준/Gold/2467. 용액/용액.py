n = int(input())
lst = list(map(int, input().split()))

s, e = 0, len(lst)-1
rst = float('inf')

while s < e:
    value = lst[s] + lst[e]
    
    if abs(value) <= rst:
        x, y = lst[s], lst[e]
        rst = abs(value)

    if value < 0:
        s += 1
    else:
        e -= 1

print(x, y)