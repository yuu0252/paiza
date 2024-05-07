n, s = map(int, input().split())
ad_list = {}
edge_num = 0

for i in range(1, n+1):
  v = int(input())
  edge_num += v
  ad_list[i] = list(map(int, input().split()))

edge_num //= 2

def dfs(v, visited, edge):
  for i in ad_list[v]:
    e = sorted((i, v))
    if e not in edge:
      visited.append(i)
      edge.append(e)
      if i == s and len(edge) == edge_num:
        print(*visited)
        exit()
      dfs(i, visited, edge)
      edge.pop()
      visited.pop()

dfs(s, [s], [])