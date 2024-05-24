n, e1, e2 = map(int, input().split())
ad_list = {}

for i in range(1, n+1):
    v = int(input())
    ad_list[i] = list(map(int, input().split()))

paths = []

def dfs(v, path):
    for i in ad_list[v]:
        if i not in path:
            path.append(i)
            dfs(i, path)
            path.pop()
        elif i == e1 and len(path) > 2:
            path.append(i)
            paths.append(tuple(path))
            path.pop()

dfs(e2, [e1, e2])

print(len(paths))