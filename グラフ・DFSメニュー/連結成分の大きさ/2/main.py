n = int(input())
ad_list = {}

for i in range(1, n+1):
  v = int(input())
  ad_list[i] = list(map(int, input().split()))

def dfs(v, path):
  for i in ad_list[v]:
    if i not in path:
      path.append(i)
      if len(path) == n:
        print("Yes")
        exit()
      else:
        dfs(i, path)

dfs(1, [1])

print("No")