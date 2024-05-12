n, s = map(int, input().split())
ad_list = {}

ans = ()

for i in range(1, n+1):
    v = int(input())
    ad_list[i] = list(map(int, input().split()))

def dfs(v, path):
    for i in ad_list[v]:
        if i not in path:
            path.append(i)
            dfs(i, path)
            path.pop()
        elif i == s:
            path.append(i)
            global ans
            if len(path) == n + 1:
                ans = tuple(path)
            path.pop()

dfs(s, [s])

if len(ans) > 0:
    print(*ans)
else:
    print(-1)