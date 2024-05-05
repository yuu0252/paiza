n, s, k = map(int, input().split())
ad_list = {}

for i in range(1, n+1):
  v = int(input())
  ad_list[i] = list(map(int, input().split()))

trails = []

def dfs(v, trail, edges):
  for i in ad_list[v]:
    e = sorted((i, v))
    if e not in edges:
      trail.append(i)
      edges.append(e)
      if len(trail) == k + 1:
        trails.append(tuple(trail))
      else:
        dfs(i, trail, edges)
      trail.pop()
      edges.pop()

dfs(s, [s], [])

print(len(trails))
for i in trails:
  print(*i)