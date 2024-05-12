n, s, t = map(int, input().split())

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
      if i == t and trail.count(s) >= 2 and trail.count(t) >= 2:
          trails.append(tuple(trail))
      dfs(i, trail, edges)
      trail.pop()
      edges.pop()

dfs(s, [s], [])

print(len(trails))
for i in trails:
  print(*i)