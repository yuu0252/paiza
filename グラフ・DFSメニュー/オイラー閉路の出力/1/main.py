import random

n, s = map(int, input().split())
ad_list = {}

for i in range(1, n+1):
  v = int(input())
  ad_list[i] = list(map(int, input().split()))

paths = []

def dfs(v, path):
  for i in ad_list[v]:
    if i not in path:
      path.append(i)
      dfs(i, path)
      path.pop()
    elif i == s and len(path) > 2:
      path.append(i)
      paths.append(tuple(path))
      path.pop()

dfs(s, [s])

if len(paths) > 0:
  print(*paths[random.randint(0, len(paths)-1)])
else:
  print(-1)