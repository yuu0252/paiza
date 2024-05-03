n, x, a, y, b, z, c = map(int, input().split())

dp = [1000*1000*1000] * (n+z)

dp[0] = 0
dp[x] = a

for i in range(x+1, n+z):
  if i >= x:
    dp[i] = min(dp[i], dp[i-x] + a)
  if i >= y:
    dp[i] = min(dp[i], dp[i-y] + b)
  if i >= z:
    dp[i] = min(dp[i], dp[i-z] + c)

print(min(dp[n:]))