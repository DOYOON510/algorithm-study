n, m = map(int, input())
lst = []
for i in range(n):
    lst.append(int(input()))

dp = [10001] * (m + 1)

for i in range(n):
    for j in range(lst[i], m + 1):
        dp[j] = min(dp[j], dp[j - lst[i]] + 1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
