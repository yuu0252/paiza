N ,M = map(int, input().split())
A = list(map(int, input().split()))
total = [0] * (N+1)

l = 0

for i in range(N):
  total[i+1] = total[i] + A[i]

start = 0
end = 0

while True:
  if end >= N:
    break
  
  if total[end+1] - total[start] <= M:
    l = max(l, end - start + 1)
    end += 1
  else:
    start += 1

print(l)