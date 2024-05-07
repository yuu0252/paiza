N, M = map(int, input().split())
A = list(map(int, input().split()))
sums = [0] * (N+1)

for i in range(N):
  sums[i+1] = sums[i] + A[i]

start = 0
end = 0
total = A[0]

l = float("inf")

while True:
  if end >= N:
    break

  if sums[end+1] - sums[start] >= M:
    l = min(l, end - start + 1)
    start += 1
  else:
    end += 1

if l == float("inf"):
  print(-1)
else:
  print(l)