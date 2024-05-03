n = int(input())
dp = [0] * (n)
A = [int(input()) for _ in range(n)]

dp[0] = 1

for i in range(1, n):
  if A[i] >= A[i-1]:
    dp[i] = dp[i-1] + 1
  else:
    dp[i] = 1

print(max(dp))