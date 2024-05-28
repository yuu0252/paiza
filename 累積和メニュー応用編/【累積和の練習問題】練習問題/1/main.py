n, a, b = map(int, input().split())
A = list(map(int, input().split()))

l = [0] * (n + 1)

for i in range(n):
  l[i+1] = l[i] + A[i]


print(l[b+1] - l[a])