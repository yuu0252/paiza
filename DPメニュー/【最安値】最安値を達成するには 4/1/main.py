N, a, b = map(int, input().split())
dp = [0] * (N+1)

dp[0] = 0
dp[1] = a

for i in range(2, N+1):
  dp[i] = min(dp[i-1] + a, dp[i-2] + b)

print(dp[N])