n, t = map(int, input().split())
k = int(input())
S = list(map(int, input().split()))

ad_list = {}

ans = ()

for i in range(1, n+1):
    v = int(input())
    ad_list[i] = list(map(int, input().split()))

for i in S:
    for j in range(1, n+1):
        if i in ad_list[j]:
            ad_list[j].remove(i)
    ad_list[i].clear()

def dfs(v, path):
    for i in ad_list[v]:
        if i not in path:
            path.append(i)
            dfs(i, path)
            path.pop()
        elif i == t and len(path) > 2:
            path.append(i)
            global ans
            if len(ans) < len(path):
                ans = tuple(path)
            path.pop()

dfs(t, [t])

if len(ans) > 0:
    print(*ans)
else:
    print(-1)