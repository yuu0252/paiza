import math
N = int(math.sqrt(10000))
A = [int(input()) for _ in range(10000)]

for i in range(0, 10000, N):
  print(max(A[i:i+N]))