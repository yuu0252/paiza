n = int(input())
ad_list = {}
for i in range(1, n+1):
    v = int(input())
    ad_list[i] = list(map(int, input().split()))

k = int(input())
for i in range(k):
    e, d = map(int, input().split())
    ad_list[e].remove(d)
    ad_list[d].remove(e)

tree = []

def dfs(v, visited):
    for i in ad_list[v]:
        if i not in visited:
            visited.append(i)
            tree.append((i, v))
            dfs(i, visited)

dfs(1, [1])

if len(tree) == n - 1:
    for t in tree:
        print(*t)
else:
    print(-1)