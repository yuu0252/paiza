n, s, t = map(int, input().split())
ad_list = {}


trails = []

for i in range(1, n+1):
  v = int(input())
  ad_list[i] = list(map(int, input().split()))

def dfs(v, trail, edges):
  for i in ad_list[v]:
    e = sorted((i, v))
    if e not in edges:
      trail.append(i)
      edges.append(e)
      if i != s:
        if i == t:
          trails.append(tuple(trail))
        else:
          dfs(i, trail, edges)
      trail.pop()
      edges.pop()

dfs(s, [s], [])

print(len(trails))
for i in trails:
  print(*i)
      
