n, x, a, y, b = map(int, input().split())

dp = [1000*1000] * (n+y)

dp[0] = 0
dp[x] = a

for i in range(x+1, n+y):
  if i >= x:
    dp[i] = min(dp[i], dp[i-x] + a)
  if i >= y:
    dp[i] = min(dp[i], dp[i-y] + b)

print(min(dp[n:]))