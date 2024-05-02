N, a, b = map(int, input().split())
dp = [10000000] * (N+5)

dp[0] = 0

for i in range(2, N+5):
  if i >= 2:
    dp[i] = min(dp[i], dp[i-2] + a)
  if i >= 5:
    dp[i] = min(dp[i], dp[i-5] + b)

print(min(dp[N:]))