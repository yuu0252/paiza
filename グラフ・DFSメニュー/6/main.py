from collections import deque

N, S, T = map(int, input().split())
K = int(input())
S_list = list(map(int, input().split()))

points = {}

for _ in range(N):
  n = int(input())
  a = list(map(int, input().split()))
  points[n] = a

q = deque()
q.append((S, [S]))

# while q:
#   now, path = q.popleft()
#   if now == T:
#     print(*path)
#   for i in points[now]:
#     if i not in path:
#       q.append((i, [*path, i]))

print(S)
print(points)