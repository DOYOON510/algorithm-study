n = int(input())
lst = list(map(int, input().split()))

rst = [0]*n
cf = sorted(set(lst))
dic = {value : i for i, value in enumerate(cf)}

for i in range(n):
    rst[i] = dic[lst[i]]

print(*rst)