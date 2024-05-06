n = int(input())
dp = [0] * n
A = [int(input()) for _ in range(n)]

dp[0] = 1

for i in range(1, n):
    dp[i] = 1
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))