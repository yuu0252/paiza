n, s, t = map(int, input().split())
ad_list = {}

for i in range(1, n+1):
  v = int(input())
  ad_list[i] = list(map(int, input().split()))

def dfs(v, path):
  for i in ad_list[v]:
    if i not in path:
      path.append(i)
      if i == t:
        print("Yes")
        exit()
      else:
        dfs(i, path)
      path.pop()

dfs(s, [s])

print("No")