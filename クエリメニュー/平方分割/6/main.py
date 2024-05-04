N, K = 10000, int(input())
A = [int(input()) for _ in range(N)]

sqrt = int(pow(N, 0.5))
if sqrt ** 2 < N:
  sqrt += 1

range_max = [-1] * sqrt
for i in range(sqrt):
  start, end = sqrt * i, sqrt * (i+1)
  range_max[i] = max(A[start:end])

for _ in range(K):
  left, right = map(lambda x:int(x) - 1, input().split())

  ans = A[left]
  now = left
  while now <= right:
    if now % sqrt == 0 and now + sqrt - 1 <= right:
      ans = max(ans, range_max[now // sqrt])
      now += sqrt
    else:
      ans = max(ans, A[now])
      now += 1

  print(ans)