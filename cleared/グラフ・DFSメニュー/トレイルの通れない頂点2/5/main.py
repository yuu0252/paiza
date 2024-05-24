n, s, t = map(int, input().split())
k = int(input())
S = set(map(int, input().split()))

ad_list = {}
trails = []

for i in range(1, n+1):
  v = int(input())
  ad_list[i] = list(map(int, input().split()))

for i in S:
  for j in ad_list[i]:
    ad_list[j].remove(i)
  ad_list[i].clear()

def dfs(v, trail, edges):
  for i in ad_list[v]:
    e = sorted((i, v))
    if e not in edges:
      trail.append(i)
      edges.append(e)
      if i == t:
        trails.append(tuple(trail))
      dfs(i, trail, edges)
      trail.pop()
      edges.pop()

dfs(s, [s], [])

print(len(trails))
for i in trails:
  print(*i)