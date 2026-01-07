n, k = map(int, input().split())

lst_a = list(map(int, input().split()))
lst_b = list(map(int, input().split()))

lst_a.sort()
lst_b.sort(reverse=True)

for i in range(k):
    if lst_a[i] < lst_b[i]:
        lst_a[i], lst_b[i] = lst_b[i], lst_a[i]
    else:
        break

print(sum(lst_a))