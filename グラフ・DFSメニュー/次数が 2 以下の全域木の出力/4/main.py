n = int(input())
k = int(input())
S = set(map(int, input().split()))

ad_list = {}

for i in range(1, n+1):
    v = int(input())
    ad_list[i] = list(map(int, input().split()))

for i in S:
    for j in ad_list[i]:
        ad_list[j].remove(i)
    ad_list[i].clear()

tree = []

def dfs(v, path):
    for i in ad_list[v]:
        if i not in path:
            path.append(i)
            tree.append((i, v))
            dfs(i, path)

vertices = set(range(1, n + 1)) - S

dfs(min(vertices), [min(vertices)])

if len(tree) == n - k - 1:
    for t in tree:
        print(*t)
else:
    print(-1)