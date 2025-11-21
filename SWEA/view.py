
for test_case in range(1, 11):
    n = int(input())
    lst = list(map(int, input().split()))
    rst = 0

    for i in range(2, n-2):
        lst2 = []
        lst2.append(lst[i] - lst[i - 1])
        lst2.append(lst[i] - lst[i - 2])
        lst2.append(lst[i] - lst[i + 1])
        lst2.append(lst[i] - lst[i + 2])
        if min(lst2) > 0:
            rst += min(lst2)
    print('#{} {}'.format(test_case, rst))
