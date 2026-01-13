n, m = map(int, input().split())
lst = list(map(int, input().split()))

while m>0:
    lst.sort()
    sum_num = sum(lst[:2])
    for i in range(2):
        lst[i] = sum_num
    m -= 1

print(sum(lst))