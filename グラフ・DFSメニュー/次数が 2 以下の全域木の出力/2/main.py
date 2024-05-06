n = int(input())
ad_list = {}
for i in range(1, n+1):
    v = int(input())
    ad_list[i] = list(map(int, input().split()))

tree = []

def dfs(v, visited):
    for i in ad_list[v]:
        if i not in visited:
            visited.append(i)
            tree.append((v, i))
            dfs(i, visited)

dfs(1, [1])
for e in tree:
    print(*e)