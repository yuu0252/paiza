N = int(input())
A = list(map(int, input().split()))
total = [0] * (N+1)

for i in range(N):
  total[i+1] = total[i] + A[i]

for i in range(N):
  print(total[i+1])