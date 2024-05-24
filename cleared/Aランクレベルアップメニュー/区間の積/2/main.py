N = int(input())
A = list(map(int, input().split()))
total = [0] * (N+1)

for i in range(N):
  total[i+1] = total[i] + A[i] 

n = int(input())

for i in range(n):
  start, end = map(int, input().split())
  print(total[end+1] - total[start])